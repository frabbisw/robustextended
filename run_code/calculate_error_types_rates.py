import json
import pdb
import pickle
from tqdm import tqdm as tq
import os
import subprocess
import jsonlines
from collections import Counter
from os import listdir
import pandas as pd
from os.path import isfile, join


def view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"])
    return prompts


def full_view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"] + json.loads(line)["canonical_solution"])
    return prompts


def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

def get_nominal_prompts(lang, type, model_name):
    if type == "nominal":
        return load_prompts(f"../datasets/{model_name}/generated_pass5_1/{lang}/nominal/f_s0.jsonl")
    elif type == "partial":
        return load_prompts(f"../datasets/{model_name}/generated_pass5_1/{lang}/partial/f_s0.jsonl")


def examine_folderpath(aug_method_path):
    file_names = [f for f in listdir(aug_method_path) if isfile(join(aug_method_path, f))]
    status_list = []
    for file_name in file_names:
        file_path = join(aug_method_path, file_name)
        prompts = load_prompts(file_path)
        for prompt in prompts:
            status_list.append(prompt["run_status_he"])
    return status_list

langs = ["java","cpp","js"]
models = ["incoder1b","incoder6b","codegen2bmulti","codegen6bmulti"]
nominals = ["nominal", "partial"]
methods = ["nlaugmenter", "natgen", "format", "func_name"]
methods_dict = {"nlaugmenter":"DocString", "natgen":"Syntax", "format":"Format", "func_name":"Function", "nominal": "Nominal", "partial": "Partial"}


def test_lang(model, lang):
    dataset_path = f"../datasets/{model}/generated_pass5_1/{lang}"
    csv_return = ""

    for method in nominals:
        method_dir = join(dataset_path, method)
        method_status = []
        method_status += examine_folderpath(method_dir)
        status_dict = Counter(method_status)
        csv_return += f"{model}, {lang}, {methods_dict[method]}, "
        for i in CODE_RUN_MESSAGE.keys():
            if i in status_dict.keys():
                csv_return += f"{round(100 * status_dict[i] / sum(status_dict.values()), 2)}"
            else:
                csv_return += "0.0"
            if i != len(CODE_RUN_MESSAGE.keys())-1:
                csv_return += ", "
        csv_return += "\n"

    for method in methods:
        method_dir = join(dataset_path, method)
        method_status = []
        for aug_method in os.listdir(method_dir):
            aug_method_path = os.path.join(method_dir,aug_method)
            aug_status = examine_folderpath(aug_method_path)
            method_status += aug_status
        status_dict = Counter(method_status)
        # print(f"Method Name: {methods_dict[method]}", end=" ")
        # for k,v in status_dict.items():
        #     print(f"{CODE_RUN_MESSAGE[k]}: {round(100*v/sum(status_dict.values()),2)}%", end=" ")
        # print()
        csv_return += f"{model}, {lang}, {methods_dict[method]}, "
        for i in CODE_RUN_MESSAGE.keys():
            if i in status_dict.keys():
                csv_return += f"{round(100*status_dict[i]/sum(status_dict.values()),2)}"
            else:
                csv_return += "0.0"
            if i != len(CODE_RUN_MESSAGE.keys())-1:
                csv_return += ", "
        csv_return += "\n"
        # for k,v in status_dict.items():
        #     print(f"{CODE_RUN_MESSAGE[k]}: {round(100*v/sum(status_dict.values()),2)}%", end=" ")
    return csv_return

CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3, "RUNTIME": 4}
CODE_RUN_MESSAGE = {0: "PASSED", 1: "ASSERTION", 2: "COMPILATION", 3: "TIMEOUT", 4: "RUNTIME"}
# CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3, "OTHER": 4}
# CODE_RUN_MESSAGE = {0: "PASSED", 1: "ASSERTION", 2: "COMPILATION", 3: "TIMEOUT", 4: "OTHER"}

stat = "model, language, method, Passed, Assertion, Compilation, Timeout, Runtime\n"

for model in models:
    # print(model)
    for lang in langs:
        # print(lang)
        res = test_lang(model, lang)
        stat += res

with open("../R/stat.csv", "w") as f:
    f.write(stat)
print(stat)