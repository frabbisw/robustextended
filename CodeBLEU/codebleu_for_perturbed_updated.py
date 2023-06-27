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

# -*- coding:utf-8 -*-
import argparse
import bleu
import weighted_ngram_match
import syntax_match
import dataflow_match

def sep(code, entry_point, data):
    if data in ["humanevalpy", "humaneval", "mbpp"]:
        single_doc = code.find("\'\'\'")
        double_doc = code.find("\"\"\"")
        if single_doc == -1:
            doc_type = "\"\"\""
        elif double_doc == -1:
            doc_type = "\'\'\'"
        elif single_doc != -1 and double_doc != -1:
            doc_type = "\"\"\""
        else:
            print("doc_type not supported!")
            exit()
        header_end = code.find('\n', code.find(entry_point))
        header = code[:header_end + 1]
        doc_begin = code.find(doc_type, header_end)
        doc_end = code.find(f"{doc_type}\n", doc_begin + 3)
        # doc_begin != -1 and doc_end != -1, means no docstring in the code, just return "" for docstring
        doc = code[header_end + 1: doc_end + 4] if doc_begin != -1 and doc_end != -1 else ""
        code = code[doc_end + 4:] if doc_begin != -1 and doc_end != -1 else code[header_end + 1:]
        # import pdb; pdb.set_trace()
        return header, doc, code
    elif data in ["humanevaljava"]:
        lines = code.split("\n")
        first_index = 0
        last_index = 0
        for i in range(len(lines)):
            if "Solution" in lines[i]:
                first_index=i
            elif entry_point in lines[i]:
                last_index=i
                # break
        # if "accepts a list of strings as a parameter" in code:
        #     import pdb; pdb.set_trace()
        return "\n".join(lines[:first_index+1])+"\n", "\n".join(lines[first_index+1:last_index])+"\n", "\n".join(lines[last_index:])
    elif data in ["humanevalcpp"]:
        if "*/" not in code:
            return "","",code
        else:
            lines = code.split("\n")
            first_index = 0
            last_index = 0
            for i in range(len(lines)):
                if "/*" in lines[i]:
                    first_index = i
                elif "*/" in lines[i]:
                    last_index = i
        return "","\n".join(lines[:last_index + 1])+"\n", "\n".join(lines[last_index + 1:])
    elif data in ["humanevaljs"]:
        if "*/" not in code:
            return "", "", code
        else:
            lines = code.split("\n")
            first_index = 0
            last_index = 0
            for i in range(len(lines)):
                if "/*" in lines[i]:
                    first_index = i
                elif "*/" in lines[i]:
                    last_index = i
        return "", "\n".join(lines[:last_index + 1]) + "\n", "\n".join(lines[last_index + 1:])
    elif data in ["humanevalgo", "mbppgo"]:
        if "//" not in code:
            entry_line = -1
            lines = code.split("\n")
            for i in range(len(lines)):
                if entry_point in lines[i]:
                    entry_line = i
                    break
            return "\n".join(lines[0:entry_line])+"\n", "", "\n".join(lines[entry_line:])
        else:
            start_point = -1
            end_point = -1
            lines = code.split("\n")
            for i in range(len(lines)):
                if "//" in lines[i]:
                    if start_point < 0:
                        start_point = i
                if entry_point in lines[i]:
                    if "func" in lines[i]:
                        end_point = i
                        break
                    else:
                        continue
            head = "\n".join(lines[0:start_point])+"\n"
            doc = "\n".join(lines[start_point:end_point])+"\n"
            test = "\n".join(lines[end_point:])
            return head, doc, test
    else:
        print(f"dataset {data} not supported")
        exit()

def load_codes(filename, lang, type):
    codes = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            entry_point = prompt["entry_point"]
            if type == "nominal":
                code = prompt["partial"]
                lines = code.split("\n")
                tmp = []
                for line in lines:
                    if "@@this" in line:
                        break
                    tmp.append(line)
                code = '\n'.join(tmp)
            else:
                code = prompt["prompt"]
            # print(code)
            header, doc, body = sep(code, entry_point, "humaneval"+lang)
            code = header + body
            codes[prompt["task_id"]] = code
    return codes


# nominals = ["nominal", "partial"]
def load_partial_paths(lang):
    methods = ["natgen", "format"]
    # nominal_path = f"../datasets/nominal/HumanEval_{lang}.jsonl"
    partial_path = f"../datasets/nominal/humaneval{lang}_partial.jsonl"

    paths_dict = {}
    paths_dict["nominal"] = partial_path
    paths_dict["perturbed"] = []

    lang_dir = f"../datasets/perturbed/humaneval{lang}/full"

    for method in methods:
        method_dir = join(lang_dir, method)
        for filename in os.listdir(method_dir):
            if "s0.jsonl" in filename:
                perturbed_path = join(method_dir, filename)
                paths_dict["perturbed"].append(perturbed_path)
    return paths_dict

def load_partial_codes(paths_dict, lang):
    perturbed_codes = {}
    nominal_codes = load_codes(paths_dict["nominal"], lang, "nominal")
    for key in nominal_codes.keys():
        perturbed_codes[key] = []

    for path in paths_dict["perturbed"]:
        contents = load_codes(path, lang, "perturbed")
        for key in perturbed_codes.keys():
            perturbed_codes[key].append(contents[key])
    return nominal_codes, perturbed_codes

def load_indivudual_partial_codes(paths_dict, lang):
    nominal_codes = load_codes(paths_dict["nominal"], lang, "nominal")
    parturbed_dict = {}
    for path in paths_dict["perturbed"]:
        perturbed_codes = {}
        for key in nominal_codes.keys():
            perturbed_codes[key] = []

        contents = load_codes(path, lang, "perturbed")
        for key in perturbed_codes.keys():
            perturbed_codes[key].append(contents[key])
        aug_method = path[path.rfind(f"humaneval{lang}")+len(f"humaneval{lang}")+1:path.find("_s0.jsonl")]
        parturbed_dict[aug_method] = perturbed_codes
    return nominal_codes, parturbed_dict

# lang = "js"
# paths_dict = load_partial_paths(lang)
# # nominal_codes, perturbed_codes = load_partial_codes(paths_dict, lang)
# nominal_codes, parturbed_dict = load_indivudual_partial_codes(paths_dict, lang)
#
#
# lang = "javascript"

# print(parturbed_dict)
# print(paths_dict)
# exit()


def make_weights(reference_tokens, key_word_list):
    return {token:1 if token in key_word_list else 0.2 \
            for token in reference_tokens}
def get_score(perturbed_codes, task_id, lang):
    alpha, beta, gamma, theta = 0.25, 0.25, 0.25, 0.25

    hypothesis = [nominal_codes[task_id].strip()]
    pre_references = [[contents.strip()] for contents in perturbed_codes[task_id]]

    max_length = max(len(p) for p in pre_references + [hypothesis])
    for i in range(len(pre_references)):
        assert len(hypothesis) == len(pre_references[i])
        if len(hypothesis) != len(pre_references[i]):
            # mx = max(len(pre_references[i]), len(hypothesis))
            pre_references[i] = pre_references[i] + ["//" for i in range(max_length - len(pre_references[i]))]
            hypothesis = hypothesis + ["//" for i in range(max_length - len(hypothesis))]
    references = []
    for i in range(len(hypothesis)):
        ref_for_instance = []
        for j in range(len(pre_references)):
            ref_for_instance.append(pre_references[j][i])
        references.append(ref_for_instance)

    ngram_match_score = bleu.corpus_bleu(references, hypothesis)


    syntax_match_score = syntax_match.corpus_syntax_match(references, hypothesis, lang)
    dataflow_match_score = dataflow_match.corpus_dataflow_match(references, hypothesis, lang)

    tokenized_hyps = [x.split() for x in hypothesis]
    tokenized_refs = [[x.split() for x in reference] for reference in references]
    ngram_match_score = bleu.corpus_bleu(tokenized_refs, tokenized_hyps)
    keywords = [x.strip() for x in open('keywords/' + lang + '.txt', 'r', encoding='utf-8').readlines()]

    tokenized_refs_with_weights = [[[reference_tokens, make_weights(reference_tokens, keywords)] for reference_tokens in reference] for reference in tokenized_refs]
    weighted_ngram_match_score = weighted_ngram_match.corpus_bleu(tokenized_refs_with_weights, tokenized_hyps)
    code_bleu_score = alpha * ngram_match_score + beta * weighted_ngram_match_score + gamma * syntax_match_score + theta * dataflow_match_score

    return syntax_match_score, dataflow_match_score, code_bleu_score

def get_result(nominal_codes, parturbed_dict, lang):
    result = ""
    result_dict = {}
    for aug_method in parturbed_dict.keys():
        syntax = []
        dataflow = []
        codebleu = []
        perturbed_codes = parturbed_dict[aug_method]
        for task_id in nominal_codes.keys():
            try:
                syntax_match_score, dataflow_match_score, code_bleu_score = get_score(perturbed_codes, task_id, lang)
                syntax.append(syntax_match_score)
                dataflow.append(dataflow_match_score)
                codebleu.append(code_bleu_score)
            except:
                None

        # print(sum(syntax)/len(syntax))
        # print(sum(dataflow)/len(dataflow))
        #
        # print("eliminating zeros in dataflow")

        syntax = [s for s in syntax if s != 0]
        dataflow = [s for s in dataflow if s != 0]
        codebleu = [s for s in codebleu if s != 0]

        # print(sum(syntax)/len(syntax))
        # print(sum(dataflow)/len(dataflow))

        # result += (aug_method + str(round(sum(syntax)/len(syntax),2) + round(sum(dataflow)/len(dataflow),2))
        # result += f"{aug_method} {round(sum(syntax)/len(syntax),2)} {round(sum(dataflow)/len(dataflow),2)}\n"
        # result_dict[aug_method] = [round(sum(syntax)/len(syntax),2), round(sum(dataflow)/len(dataflow),2), round(sum(codebleu)/len(codebleu),2)]
        result_dict[aug_method] = [round(sum(syntax) / len(syntax), 2), round(sum(dataflow) / len(dataflow), 2)]
        # break
    return result_dict

lang_map = {"java":"java","cpp":"cpp","js":"javascript"}
# langs = ["java","cpp","js"]
langs = ["cpp"]

dicts = []
for lang in langs:
    paths_dict = load_partial_paths(lang)
    nominal_codes, parturbed_dict = load_indivudual_partial_codes(paths_dict, lang)
    result_dict = get_result(nominal_codes, parturbed_dict, lang_map[lang])
    dicts.append(result_dict)

for i in range(1, len(dicts)):
    result_dict = dicts[i]
    for key in dicts[0].keys():
        dicts[0][key] = dicts[0][key] + result_dict[key]

values = [0,0,0,0,0,0]
for key in dicts[0].keys():
    if key in ["ForWhileTransformer", "OperandSwap", "DeadCodeInserter", "VarRenamerRN", "VarRenamerCB", "VarRenamerNaive"]:
        cat = "Syntax"
    else:
        cat = "Format"
    print(f"{cat} & " + key.replace("_","\_"), end = " ")
    index = 0
    for v in dicts[0][key]:
        values[index] += v
        index += 1
        print(f"& {v}", end=" ")
    print("\\\\")
import numpy as np
print(np.array(values)/12)