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
    # print(prompts)
    # exit()
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

def get_nominal_prompts(lang, type):
    if type == "nominal":
        return load_prompts(f"../datasets/codegen6bmulti/generated_pass5_1/{lang}/nominal/f_s0.jsonl")
    elif type == "partial":
        return load_prompts(f"../datasets/codegen6bmulti/generated_pass5_1/{lang}/partial/f_s0.jsonl")

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

def calculate_metrics_summary(K, lang, model_name):
    result_dict = {}
    fake_dict = {}
    result_dict["method"] = ["RP@k", "RD@k", "RR@k"]
    fake_dict["method"] = ["RP@k", "RD@k", "RR@k"]
    datasets_path = f"../datasets/{model_name}/generated_pass5_1"
    methods = ["nlaugmenter", "natgen", "format", "func_name"]
    # langs = ["java"]
    nominal_passatk_dict = get_nominal_passatk_dict(lang, "nominal")
    partial_passatk_dict = get_nominal_passatk_dict(lang, "partial")

    nominal_passatk = calculate_passatk(nominal_passatk_dict)
    partial_passatk = calculate_passatk(partial_passatk_dict)

    result_dict["nominal"] = round(nominal_passatk, 2)
    result_dict["partial"] = round(partial_passatk, 2)

    fake_dict["nominal"] = "."
    fake_dict["partial"] = "."

    lang_path = os.path.join(datasets_path, lang)
    for method in methods:
        drop_list = []
        relative_list = []
        method_path = os.path.join(lang_path, method)

        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            passatk_worst_dict = get_worst_passatk_dict(aug_method_path, K)
            drop_list.append(passatk_worst_dict)
            if method in ["natgen", "format"]:
                relative_list.append([passatk_worst_dict, partial_passatk_dict])
            elif method in ["nlaugmenter", "func_name"]:
                relative_list.append([passatk_worst_dict, nominal_passatk_dict])

        passatk_worst = calculate_passatk_summary(drop_list)
        if method in ["natgen", "format"]:
            robust_drop = (partial_passatk - passatk_worst) / partial_passatk
        else:
            robust_drop = (nominal_passatk - passatk_worst) / nominal_passatk
        robust_relative = get_relative_passatk_summary(relative_list)
        result_dict[method] = [round(passatk_worst, 2), round(robust_drop, 2), round(robust_relative, 2)]
        fake_dict[method] = [".", ".", "."]

    return result_dict, fake_dict


def calculate_metrics(K, lang, model_name):
    result_dict = {}
    fake_dict = {}
    result_dict["aug_method"] = ["RP@k", "RD@k", "RR@k"]
    fake_dict["aug_method"] = ["RP@k", "RD@k", "RR@k"]
    datasets_path = f"../datasets/{model_name}/generated_pass5_1"
    methods = ["nlaugmenter", "natgen", "format", "func_name"]
    # langs = ["java"]
    nominal_passatk_dict = get_nominal_passatk_dict(lang, "nominal")
    partial_passatk_dict = get_nominal_passatk_dict(lang, "partial")

    nominal_passatk = calculate_passatk(nominal_passatk_dict)
    partial_passatk = calculate_passatk(partial_passatk_dict)

    result_dict["nominal"] = round(nominal_passatk, 2)
    result_dict["partial"] = round(partial_passatk, 2)

    fake_dict["nominal"] = "."
    fake_dict["partial"] = "."

    lang_path = os.path.join(datasets_path, lang)
    for method in methods:
        method_path = os.path.join(lang_path, method)

        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path, aug_method)
            passatk_worst_dict = get_worst_passatk_dict(aug_method_path, K)
            passatk_worst = calculate_passatk(passatk_worst_dict)
            if method in ["natgen", "format"]:
                robust_drop = (partial_passatk - passatk_worst) / partial_passatk
                robust_relative = get_relative_passatk(passatk_worst_dict, partial_passatk_dict)
            elif method in ["nlaugmenter", "func_name"]:
                robust_drop = (nominal_passatk - passatk_worst) / nominal_passatk
                robust_relative = get_relative_passatk(passatk_worst_dict, nominal_passatk_dict)
            result_dict[aug_method] = [round(passatk_worst, 2), round(robust_drop, 2), round(robust_relative, 2)]
            fake_dict[aug_method] = [".", ".", "."]
            # print(f"Lang: {lang}, Method: {method}, style: {aug_method}, worst: {round(passatk_worst, 2)}, drop: {round(robust_drop, 2)}, relative: {round(robust_relative, 2)}")
            # print("\\multirow{3}{*}{\\centering TenseTransformationFuture} & RP{\\footnotesize5}@1 & 0 & 0 & 0  & 0 & 0 & 0 & 0 & 0 & 0\\\\")
    return result_dict, fake_dict

def prepare_overleaf_table(model_dict):
    aug_dict = {}
    nominal_dict = {}
    nominal_dict["nominal"] = []
    nominal_dict["partial"] = []

    for model_name in model_dict.keys():
        for lang_dict in model_dict[model_name]:
            nominal_dict["nominal"].append(lang_dict["nominal"])
            nominal_dict["partial"].append(lang_dict["partial"])
            for aug_method in lang_dict.keys():
                if aug_method in ["nominal", "partial"]:
                    continue
                if aug_method not in aug_dict.keys():
                    aug_dict[aug_method] = {"rpk":[], "rdk":[], "rrk":[]}
                passatk_worst, robust_drop, robust_relative = lang_dict[aug_method]
                aug_dict[aug_method]["rpk"].append(passatk_worst)
                aug_dict[aug_method]["rdk"].append(robust_drop)
                aug_dict[aug_method]["rrk"].append(robust_relative)

                # passatk_worst, robust_drop, robust_relative = lang_dict[aug_method]
                # print("\\multirow{3}{*}{\\centering aug_method} & RP{\\footnotesize5}@1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\\")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|p{6cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|}")
    print("\t\\hline")
    print("\t0 & Model & \\multicolumn{3}{|p{4cm}|}{\\centering Incoder-1B} & \\multicolumn{3}{|p{4cm}|}{\\centering CodeGen-2B-multi} & \\multicolumn{3}{|p{4cm}|}{\\centering CodeGen-6B-multi} \\\\")
    print("\t\\hline")
    print("\tPerturbation & Metric & Java & CPP & JS & Java & CPP & JS & Java & CPP & JS \\\\")
    print("\t\\hline")

    print("\tNominal & RP{\\footnotesize5}@1 ", end = "")
    for v in nominal_dict["nominal"]:
        print(f"& {v} ", end="")
    print("\\\\")

    print("\t\\hline")

    print("\tPartial & RP{\\footnotesize5}@1 ", end="")
    for v in nominal_dict["partial"]:
        print(f"& {v} ", end="")
    print("\\\\")

    print("\t\\hline")

    for key in aug_dict.keys():
        # if key in ["nominal", "partial"]:
        #     continue
        print("\t\\multirow{3}{*}{\\centering "+key.replace("_","\\_")+"} & RP{\\footnotesize5}@1", end = " ")
        for v in aug_dict[key]["rpk"]:
            print(f"& {v}", end = " ")
        print("\\\\")

        print("\t& RD{\\footnotesize5}@1 ", end = " ")
        for v in aug_dict[key]["rdk"]:
            print(f"& {v}", end = " ")
        print("\\\\")

        print("\t& RR{\\footnotesize5}@1 ", end = " ")
        for v in aug_dict[key]["rrk"]:
            print(f"& {v}", end=" ")
        print("\\\\")
        print("\t\\hline")

        # print(key, aug_dict[key]["rpk"])
        # print(key, aug_dict[key]["rdk"])
        # print(key, aug_dict[key]["rrk"])
        # print("*"*100)



# java_dict_6b, fake_dict = calculate_metrics(5, "java", "codegen6bmulti")
# cpp_dict_6b, _ = calculate_metrics(5, "cpp", "codegen6bmulti")
# js_dict_6b, _ = calculate_metrics(5, "js", "codegen6bmulti")


# codegen6bmulti = [java_dict_6b, cpp_dict_6b, js_dict_6b]
# incoder1b = [fake_dict, fake_dict, fake_dict]
# codegen2bmulti = [fake_dict, fake_dict, fake_dict]
#
# model_dict = {"Incoder-1B": incoder1b, "CodeGen-2B-multi": codegen2bmulti, "CodeGen-6B-multi": codegen6bmulti}
# prepare_overleaf_table(model_dict)

def prepare_overleaf_table_summary(model_dict):
    method_dict = {}
    nominal_dict = {}
    nominal_dict["nominal"] = []
    nominal_dict["partial"] = []
    method_map = {"natgen":"Syntax", "format":"Format", "nlaugmenter":"DocString", "func_name":"Function", "method":"method"}
    for model_name in model_dict.keys():
        for lang_dict in model_dict[model_name]:
            nominal_dict["nominal"].append(lang_dict["nominal"])
            nominal_dict["partial"].append(lang_dict["partial"])
            for method in lang_dict.keys():
                if method in ["nominal", "partial"]:
                    continue
                try:
                    if method_map[method] not in method_dict.keys():
                        method_dict[method_map[method]] = {"rpk":[], "rdk":[], "rrk":[]}
                except:
                    print(method)
                    exit()
                passatk_worst, robust_drop, robust_relative = lang_dict[method]
                method_dict[method_map[method]]["rpk"].append(passatk_worst)
                method_dict[method_map[method]]["rdk"].append(robust_drop)
                method_dict[method_map[method]]["rrk"].append(robust_relative)

                # passatk_worst, robust_drop, robust_relative = lang_dict[aug_method]
                # print("\\multirow{3}{*}{\\centering aug_method} & RP{\\footnotesize5}@1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\\\")
    print("\\resizebox{\\textwidth}{!}{\\begin{tabular}{|p{6cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|}")
    print("\t\\hline")
    print("\t0 & Model & \\multicolumn{3}{|p{4cm}|}{\\centering Incoder-1B} & \\multicolumn{3}{|p{4cm}|}{\\centering CodeGen-2B-multi} & \\multicolumn{3}{|p{4cm}|}{\\centering CodeGen-6B-multi} \\\\")
    print("\t\\hline")
    print("\tPerturbation & Metric & Java & CPP & JS & Java & CPP & JS & Java & CPP & JS \\\\")
    print("\t\\hline")

    print("\tNominal & RP{\\footnotesize5}@1 ", end = "")
    for v in nominal_dict["nominal"]:
        print(f"& {v} ", end="")
    print("\\\\")

    print("\t\\hline")

    print("\tPartial & RP{\\footnotesize5}@1 ", end="")
    for v in nominal_dict["partial"]:
        print(f"& {v} ", end="")
    print("\\\\")

    print("\t\\hline")

    for key in method_dict.keys():
        # if key in ["nominal", "partial"]:
        #     continue
        if key in ["Syntax", "Format"]:
            tmp = nominal_dict["partial"]
        else:
            tmp = nominal_dict["nominal"]
        print("\t\\multirow{4}{*}{\\centering " + key.replace("_", "\\_") + "} & Nominal$\\uparrow$", end=" ")
        for v in tmp:
            print(f"& {v} ", end="")
        print("\\\\")

        print("\t& RP{\\footnotesize5}@1$\\uparrow$ ", end = " ")
        for v in method_dict[key]["rpk"]:
            print(f"& {v}", end = " ")
        print("\\\\")

        print("\t& RD{\\footnotesize5}@1$\\downarrow$ ", end = " ")
        for v in method_dict[key]["rdk"]:
            print(f"& {v}", end = " ")
        print("\\\\")

        print("\t& RR{\\footnotesize5}@1$\\downarrow$ ", end = " ")
        for v in method_dict[key]["rrk"]:
            print(f"& {v}", end=" ")
        print("\\\\")
        print("\t\\hline")

java_sum_6b, fake_dict = calculate_metrics_summary(5, "java", "codegen6bmulti")
cpp_sum_6b, fake_dict = calculate_metrics_summary(5, "cpp", "codegen6bmulti")
js_sum_6b, fake_dict = calculate_metrics_summary(5, "js", "codegen6bmulti")


codegen6bmulti = [java_sum_6b, cpp_sum_6b, js_sum_6b]
incoder1b = [fake_dict, fake_dict, fake_dict]
codegen2bmulti = [fake_dict, fake_dict, fake_dict]
#
model_dict = {"Incoder-1B": incoder1b, "CodeGen-2B-multi": codegen2bmulti, "CodeGen-6B-multi": codegen6bmulti}
prepare_overleaf_table_summary(model_dict)


# print(java_sum_6b)