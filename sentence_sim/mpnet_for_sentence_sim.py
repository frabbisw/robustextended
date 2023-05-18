# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import json
import pdb
import pickle
from tqdm import tqdm as tq
import os
import subprocess
import jsonlines
from collections import Counter
from os import listdir
from os.path import isfile, join

def sep_doc(data, prompt, entry_point):
    """ A help function to seperate docstring, a specific function for MBXP and humaneval
    Note that there is another sep function in natgen which is used to seperate
    the whole documents in prompt including docstring & examples.
    """
    # sep into header, docstring only (without any special charaters like """), examples
    if data in ["humaneval", "mbpp", "humanevalpy", "humanevaljava", "humanevalcpp", "humanevaljs", "humanevalgo", "mbgo"]:
        if data in ["humanevalgo", "mbgo"]:
            start_point = -1
            end_point = -1
            lines = prompt.split("\n")
            for i in range(len(lines)):
                if "//" in lines[i]:
                    if start_point < 0:
                        start_point = i
                if entry_point in lines[i]:
                    end_point = i
                    break
            head = "\n".join(lines[0:start_point])+"\n"
            doc = "\n".join(lines[start_point:end_point])
            doc = doc.replace("// ", "")
            doc = doc.replace("//", "")
            test = "\n"+"\n".join(lines[end_point:])
            return head, doc, test

        elif data in ["humanevalpy", "humaneval", "mbpp"]:
            doc_start_sign = '"""'
            doc_start_sign_alt = '\'\'\''
            start_limit = prompt.find(entry_point)
        elif data in ["humanevaljava", "humanevalcpp", "humanevaljs", "mbjp", "mbjsp", "mbcp"]:
            doc_start_sign = '/*'
            doc_start_sign_alt = '//'
            start_limit = 0
        start = prompt.find(doc_start_sign, start_limit)
        if start == -1: # some humaneval will use "'''" for docstrings
            start = prompt.find(doc_start_sign_alt, start_limit)

        # import pdb;
        # pdb.set_trace()

        assert start != -1
        start = start + 2
        # some transformation might remove \n, so we need to keep \n \t in head part
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find(">>>", start_limit)
        if end == -1: #some docstring has no >>> string. instead they have for example, example strings
            end = prompt.lower().find("for example", start_limit)
        if end == -1:
            end = prompt.lower().find("example", start_limit)

        # some transformation might remove \n, so we need to keep \n \t in cases part
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1

        # import pdb;
        # pdb.set_trace()

        return prompt[:start], prompt[start:end], prompt[end:]

    # elif data in ["humanevalcpp"]:
    #     import pdb;
    #     pdb.set_trace()
    #     return "dummy"

    elif data in ["mbjp", "mbjsp", "mbjp", "mbjsp", "mbcp"]:
        # start = prompt.find('/**', prompt.find(entry_point))
        start = prompt.find('/**')
        assert start != -1
        start = start + 3
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find("* >")
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1
        return prompt[:start], prompt[start:end], prompt[end:]
    elif data in ["mbphp", "mbkp", "mbrbp"]:
        if data == "mbphp":
            start_flag = "You are an expert PHP programmer, and here is your task.\n *"
            end_flag = "* php >"
        elif data == "mbkp":
            start_flag = "You are an expert Kotlin programmer, and here is your task.\n *"
            end_flag = "* >>>"
        elif data == "mbrbp":
            start_flag = "You are an expert Ruby programmer, and here is your task.\n#"
            end_flag = "# irb>"
        start = prompt.find(start_flag) + len(start_flag)
        special = start + 1
        while prompt[special] in [" ", "\n", "\t", "*"]:
            special += 1
        start = special
        end = prompt.find(end_flag)
        special = end - 1
        while prompt[special] in [" ", "\n", "\t"]:
            special -= 1
        end = special + 1
        return prompt[:start], prompt[start:end], prompt[end:]
    else:
        print(f"Dataset {data} not supported for transformation!")
        exit()

def load_docstrings(filename, lang):
    prompts = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)

            entry_point = prompt["entry_point"]
            docstring = prompt["prompt"]

            head, doc, cases = sep_doc("humaneval"+lang, docstring, entry_point)
            prompts[prompt["task_id"]] = doc.strip()
    return prompts

def load_entry_points(filename, lang):
    entry_points = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            entry_points[prompt["task_id"]] = prompt["entry_point"]
    return entry_points

def load_paths(lang, method):
    nominal_path = f"../datasets/nominal/HumanEval_{lang}.jsonl"

    paths_dict = {}
    paths_dict["nominal"] = nominal_path
    paths_dict["perturbed"] = []

    lang_dir = f"../datasets/perturbed/humaneval{lang}/full"

    method_dir = join(lang_dir, method)
    for filename in os.listdir(method_dir):
        if "s0.jsonl" in filename:
            perturbed_path = join(method_dir, filename)
            paths_dict["perturbed"].append(perturbed_path)
    return paths_dict

def load_all_docstrings(paths_dict, lang):
    nominal_docstrings = load_docstrings(paths_dict["nominal"], lang)
    perturbed_doc_dict = {}
    for path in paths_dict["perturbed"]:
        perturbed_docstrings = {}
        for key in nominal_docstrings.keys():
            perturbed_docstrings[key] = []
        contents = load_docstrings(path, lang)
        for key in perturbed_docstrings.keys():
            perturbed_docstrings[key].append(contents[key])
        aug_method = path[path.rfind(f"humaneval{lang}") + len(f"humaneval{lang}") + 1:path.find("_s0.jsonl")]
        perturbed_doc_dict[aug_method] = perturbed_docstrings
    return nominal_docstrings, perturbed_doc_dict

def load_all_entry_points(paths_dict, lang):
    nominal_entry_points = load_entry_points(paths_dict["nominal"], lang)
    perturbed_entry_dict = {}
    for path in paths_dict["perturbed"]:
        perturbed_entry_points = {}
        for key in nominal_entry_points.keys():
            perturbed_entry_points[key] = []
        contents = load_entry_points(path, lang)
        for key in perturbed_entry_points.keys():
            perturbed_entry_points[key].append(contents[key])
        aug_method = path[path.rfind(f"humaneval{lang}") + len(f"humaneval{lang}") + 1:path.find("_s0.jsonl")]
        perturbed_entry_dict[aug_method] = perturbed_entry_points
    return nominal_entry_points, perturbed_entry_dict

import pickle

langs = ["java","cpp","js"]

for lang in langs:
    paths_dict_d = load_paths(lang, "nlaugmenter")
    paths_dict_e = load_paths(lang, "func_name")

    nominal_docstrings, perturbed_doc_dict = load_all_docstrings(paths_dict_d, lang)
    nominal_entry_points, perturbed_entry_dict = load_all_entry_points(paths_dict_e, lang)

    with open(f"nominal_docstrings{lang}.pkl", "wb") as f:
        pickle.dump(nominal_docstrings, f)

    with open(f"perturbed_doc_dict{lang}.pkl", "wb") as f:
        pickle.dump(perturbed_doc_dict, f)

    with open(f"nominal_entry_points{lang}.pkl", "wb") as f:
        pickle.dump(nominal_entry_points, f)

    with open(f"perturbed_entry_dict{lang}.pkl", "wb") as f:
        pickle.dump(perturbed_entry_dict, f)

    # print(perturbed_entry_dict.keys())
    # exit()
# import pdb; pdb.set_trace()

