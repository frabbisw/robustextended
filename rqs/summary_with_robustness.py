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
import  numpy as np
from scipy.stats import fisher_exact
from scipy.stats import chisquare
import pickle

DATASET_PATH = "/home/f_rabbi/recode/extended_all_results/datasets-backup"

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
    # print(prompts)
    # exit()
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

def get_nominal_prompts(lang, type, model_name):
    if type == "nominal":
        return load_prompts(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/nominal/f_s0.jsonl")
    elif type == "partial":
        return load_prompts(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/partial/f_s0.jsonl")

def calculate_passatk(data):
    return sum(data.values()) / len(data)
def get_nominal_passatk_dict(lang, type, model_name):
    prompts = get_nominal_prompts(lang, type, model_name)
    passatk = {}
    for prompt in prompts:
        if "passed_evalplus" not in prompt.keys():
            print(lang, type, model_name)
            print(prompt)
            exit(1)
        passatk[prompt["task_id"]] = prompt["passed_evalplus"]
    return passatk
def get_worst_passatk_dict(directory, K):
    perturbed_list = []
    passatk_worst = {}
    for i in range(K):
        filepath = join(directory, f"f_s{i}.jsonl")
        perturbed_list.append(load_prompts(filepath))

    for prompt in perturbed_list[0]:
        passatk_worst[prompt["task_id"]] = 1

    for i in range(K):
        for prompt in perturbed_list[i]:
            passatk_worst[prompt["task_id"]] = passatk_worst[prompt["task_id"]] and prompt["passed_evalplus"]

    return passatk_worst
def get_custom_passatk_dict(directory, K, T):
    perturbed_list = []
    passatk_custom = {}
    for i in range(K):
        filepath = join(directory, f"f_s{i}.jsonl")
        perturbed_list.append(load_prompts(filepath))

    for prompt in perturbed_list[0]:
        passatk_custom[prompt["task_id"]] = 0

    for i in range(K):
        for prompt in perturbed_list[i]:
            passatk_custom[prompt["task_id"]] = passatk_custom[prompt["task_id"]] + prompt["passed_evalplus"]
            # print(passatk_custom[prompt["task_id"]] + prompt["passed"])

    for prompt in perturbed_list[i]:
        # print(passatk_custom[prompt["task_id"]], T)
        if passatk_custom[prompt["task_id"]] >= T:
            passatk_custom[prompt["task_id"]] = 1
        else:
            passatk_custom[prompt["task_id"]] = 0
        # print(passatk_custom[prompt["task_id"]])

    return passatk_custom
def get_relative_passatk(passatk_worst_dict, nominal_passatk_dict):
    assert len(passatk_worst_dict) == len(nominal_passatk_dict)
    cnt = 0
    for key in passatk_worst_dict.keys():
        if passatk_worst_dict[key] != nominal_passatk_dict[key]:
            cnt += 1
    return cnt/len(passatk_worst_dict)


def calculate_passatk_summary(drop_list):
    passes = 0
    total = 0
    for data in drop_list:
        passes += sum(data.values())
        total += len(data)
    return passes/total

def get_relative_passatk_summary(relative_list):
    not_equal = 0
    total = 0
    for passatk_worst_dict, nominal_passatk_dict in relative_list:
        total += len(nominal_passatk_dict.keys())
        assert len(passatk_worst_dict) == len(nominal_passatk_dict)
        for key in passatk_worst_dict.keys():
            if passatk_worst_dict[key] != nominal_passatk_dict[key]:
                not_equal += 1
    return not_equal/total

def calculate_metrics_summary(K, T, lang, model_name):
    result_dict = {}
    fake_dict = {}
    result_dict["method"] = ["RP@k", "RD@k", "RR@k"]
    fake_dict["method"] = ["RP@k", "RD@k", "RR@k"]
    datasets_path = f"{DATASET_PATH}/{model_name}/generated_pass5_1"
    methods = ["nlaugmenter", "natgen", "format", "func_name"]
    # langs = ["java"]
    nominal_passatk_dict = get_nominal_passatk_dict(lang, "nominal", model_name)
    partial_passatk_dict = get_nominal_passatk_dict(lang, "partial", model_name)

    nominal_passatk = calculate_passatk(nominal_passatk_dict)
    partial_passatk = calculate_passatk(partial_passatk_dict)

    result_dict["nominal"] = nominal_passatk
    result_dict["partial"] = partial_passatk

    fake_dict["nominal"] = "."
    fake_dict["partial"] = "."

    lang_path = os.path.join(datasets_path, lang)
    for method in methods:
        drop_list = []
        relative_list = []
        method_path = os.path.join(lang_path, method)

        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            # passatk_worst_dict = get_worst_passatk_dict(aug_method_path, K)
            passatk_worst_dict = get_custom_passatk_dict(aug_method_path, K, T)
            drop_list.append(passatk_worst_dict)
            if method in ["natgen", "format"]:
                relative_list.append([passatk_worst_dict, partial_passatk_dict])
            elif method in ["nlaugmenter", "func_name"]:
                relative_list.append([passatk_worst_dict, nominal_passatk_dict])

        passatk_worst = calculate_passatk_summary(drop_list)
        # if passatk_worst > 0:
        #     print(method)
        #     print(drop_list)
        #     print("*"*50)

        try:
            if method in ["natgen", "format"]:
                robust_drop = (partial_passatk - passatk_worst) / partial_passatk
            else:
                robust_drop = (nominal_passatk - passatk_worst) / nominal_passatk
        except:
            robust_drop = 0

        robust_relative = get_relative_passatk_summary(relative_list)
        # nominal_passatk = round(nominal_passatk, 2)
        # partial_passatk = round(partial_passatk, 2)
        # passatk_worst = round(passatk_worst, 2)
        # robust_drop = robust_drop

        result_dict[method] = [passatk_worst, robust_drop, robust_relative]
        fake_dict[method] = [".", ".", "."]


    return result_dict, fake_dict

K = 5
T = 5

sample_size = 164

java_sum_6b, fake_dict = calculate_metrics_summary(K, T, "java", "codegen6bmulti")
cpp_sum_6b, fake_dict = calculate_metrics_summary(K, T, "cpp", "codegen6bmulti")
js_sum_6b, fake_dict = calculate_metrics_summary(K, T, "js", "codegen6bmulti")

java_sum_2b, fake_dict = calculate_metrics_summary(K, T, "java", "codegen2bmulti")
cpp_sum_2b, fake_dict = calculate_metrics_summary(K, T, "cpp", "codegen2bmulti")
js_sum_2b, fake_dict = calculate_metrics_summary(K, T, "js", "codegen2bmulti")

java_sum_1b, fake_dict = calculate_metrics_summary(K, T, "java", "incoder1b")
cpp_sum_1b, fake_dict = calculate_metrics_summary(K, T, "cpp", "incoder1b")
js_sum_1b, fake_dict = calculate_metrics_summary(K, T, "js", "incoder1b")

java_sum_in, fake_dict = calculate_metrics_summary(K, T, "java", "incoder6b")
cpp_sum_in, fake_dict = calculate_metrics_summary(K, T, "cpp", "incoder6b")
js_sum_in, fake_dict = calculate_metrics_summary(K, T, "js", "incoder6b")

java_sum_qn, fake_dict = calculate_metrics_summary(K, T, "java", "qwencoder")
cpp_sum_qn, fake_dict = calculate_metrics_summary(K, T, "cpp", "qwencoder")
js_sum_qn, fake_dict = calculate_metrics_summary(K, T, "js", "qwencoder")

java_sum_mg, fake_dict = calculate_metrics_summary(K, T, "java", "magicoder7b")
cpp_sum_mg, fake_dict = calculate_metrics_summary(K, T, "cpp", "magicoder7b")
js_sum_mg, fake_dict = calculate_metrics_summary(K, T, "js", "magicoder7b")

model_dict = {
    "codegen6bmulti": {
        "java": java_sum_6b,
        "cpp": cpp_sum_6b,
        "js": js_sum_6b
    },
    "incoder1b": {
        "java": java_sum_1b,
        "cpp": cpp_sum_1b,
        "js": js_sum_1b
    },
    "incoder6b": {
        "java": java_sum_in,
        "cpp": cpp_sum_in,
        "js": js_sum_in
    },
    "codegen2bmulti": {
        "java": java_sum_2b,
        "cpp": cpp_sum_2b,
        "js": js_sum_2b
    },
    "qwencoder": {
        "java": java_sum_qn,
        "cpp": cpp_sum_qn,
        "js": js_sum_qn
    },
    "magicoder7b": {
        "java": java_sum_mg,
        "cpp": cpp_sum_mg,
        "js": js_sum_mg
    }
}

with open("stat_list.pkl", "rb") as f:
    stat_list = pickle.load(f)
    
for i, s in enumerate(stat_list):
    model_name, lang, pert_type = stat_list[i]["model_name"], stat_list[i]["lang"], stat_list[i]["pert_type"]
    stat_list[i]["robust_drop"] = model_dict[model_name][lang][pert_type][1]

key_identity = ["model_name", "pert_type"]
key_metrics = ["func_name_change", "docstring_change", "code_change", "prompt_change", "generated_code_change", "nominal_LOC", "perturbed_LOC", "nominal_tokens", "perturbed_tokens", "nominal_complexity", "perturbed_complexity"]
key_columns = ["run_status", "lang"]
robust_column = ["robust_drop"]

column_names = key_identity + key_metrics + key_columns + robust_column

def get_a_short_list(stat_list, keys):
    ret_list = []
    for s in stat_list:
        row = []
        for k in keys:
            row.append(s[k])
        # for c in key_columns:
        #     row.append(s[c])
        ret_list.append(row)
    return ret_list

data_with_robust = [column_names] + get_a_short_list(stat_list, column_names)

with open("stat_with_robust.pkl", "wb") as f:
    pickle.dump(stat_list, f)
    
with open("data_with_robust.pkl", "wb") as f:
    pickle.dump(data_with_robust, f)
