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

def get_nominal_prompts(lang, type):
    if type == "nominal":
        return load_prompts(f"../datasets/generated_pass5_1/{lang}/nominal/nominal_temp_2.jsonl")
    elif type == "partial":
        return load_prompts(f"../datasets/generated_pass5_1/{lang}/partial/partial_temp_2.jsonl")

def calculate_passatk(data):
    return sum(data.values()) / len(data)
def get_nominal_passatk_dict(lang, type):
    prompts = get_nominal_prompts(lang, type)
    passatk = {}
    for prompt in prompts:
        passatk[prompt["task_id"]] = prompt["passed"]
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
            passatk_worst[prompt["task_id"]] = passatk_worst[prompt["task_id"]] and prompt["passed"]

    return passatk_worst
def get_relative_passatk(passatk_worst_dict, nominal_passatk_dict):
    assert len(passatk_worst_dict) == len(nominal_passatk_dict)
    cnt = 0
    for key in passatk_worst_dict.keys():
        if passatk_worst_dict[key] != nominal_passatk_dict[key]:
            cnt += 1
    return cnt/len(passatk_worst_dict)

def calculate_metrics(K):
    datasets_path = "../datasets/generated_pass5_1"
    methods = ["nlaugmenter", "natgen", "format", "func_name"]
    langs = ["cpp"]
    K = 5
    for lang in langs:
        nominal_passatk_dict = get_nominal_passatk_dict(lang, "nominal")
        partial_passatk_dict = get_nominal_passatk_dict(lang, "partial")

        nominal_passatk = calculate_passatk(nominal_passatk_dict)
        partial_passatk = calculate_passatk(partial_passatk_dict)

        lang_path = os.path.join(datasets_path, lang)
        for method in methods:
            method_path = os.path.join(lang_path, method)
            for aug_method in os.listdir(method_path):
                aug_method_path = os.path.join(method_path,aug_method)
                passatk_worst_dict = get_worst_passatk_dict(aug_method_path, K)
                passatk_worst = calculate_passatk(passatk_worst_dict)
                if method in ["natgen", "format"]:
                    robust_drop = (partial_passatk - passatk_worst) / partial_passatk
                    robust_relative = get_relative_passatk(passatk_worst_dict, partial_passatk_dict)
                elif method in ["nlaugmenter", "func_name"]:
                    robust_drop = (nominal_passatk - passatk_worst) / nominal_passatk
                    robust_relative = get_relative_passatk(passatk_worst_dict, nominal_passatk_dict)
                print(f"Lang: {lang}, Method: {method}, style: {aug_method}, worst: {round(passatk_worst, 2)}, drop: {round(robust_drop, 2)}, relative: {round(robust_relative, 2)}")

calculate_metrics(5)