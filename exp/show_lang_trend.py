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

codegen6bmulti = [java_sum_6b, cpp_sum_6b, js_sum_6b]
incoder1b = [java_sum_1b, cpp_sum_1b, js_sum_1b]
incoder6b = [java_sum_in, cpp_sum_in, js_sum_in]
codegen2bmulti = [java_sum_2b, cpp_sum_2b, js_sum_2b]
qwencoder = [java_sum_qn, cpp_sum_qn, js_sum_qn]
magicoder7b = [java_sum_mg, cpp_sum_mg, js_sum_mg]

# model_dict = {"Incoder-1B": incoder1b, "Incoder-6B": incoder6b, "CodeGen-2B-multi": codegen2bmulti, "CodeGen-6B-multi": codegen6bmulti}
# model_dict = {"Incoder-1B": incoder1b, "Incoder-6B": incoder6b, "CodeGen-2B-multi": codegen2bmulti, "CodeGen-6B-multi": codegen6bmulti, "Magicoder-7B": magicoder7b, "QwenCoder": qwencoder}
# model_dict = {"Magicoder-7B": magicoder7b, "QwenCoder": qwencoder, "Magicoder-7B": magicoder7b, "QwenCoder": qwencoder}

import matplotlib.pyplot as plt

# Example structure (replace with your actual 6 datasets)
models = [incoder1b, incoder6b, codegen2bmulti, codegen6bmulti, qwencoder, magicoder7b]
model_names = ["Incoder-1B", "Incoder-6B", "CodeGen-2B-Multi", "CodeGen-6B-Multi", "QwenCode", "Magicoder-7B"]

def show_six_plots(models, model_names):
    languages = ["Java", "C++", "JS"]
    # perturbations = ["nlaugmenter", "natgen", "format", "func_name"]
    perturbations = ["DocString", "Syntax", "Format", "FuncName"]
    colors = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()
    
    for i, (ax, model_data, model_name) in enumerate(zip(axes, models, model_names)):
        for lang_data, lang_label in zip(model_data, languages):
            nominal = lang_data["nominal"]
            for pert, color in zip(perturbations, colors):
                rd_val = lang_data[pert][1]  # RD@k
                ax.scatter(nominal, rd_val, color=color, s=60, alpha=0.8)
                ax.text(nominal + 0.005, rd_val, lang_label, fontsize=7)
    
        ax.plot([0, 1], [0, 1], "k--", alpha=0.4)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title(model_name, fontsize=12)
        ax.set_xlabel("Nominal", fontsize=10)
        ax.set_ylabel("RD@k", fontsize=10)
        ax.grid(alpha=0.3)
    
    # Single legend for all subplots
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, label=p, markersize=8)
               for c, p in zip(colors, perturbations)]
    fig.legend(handles=handles, loc='lower center', ncol=4, fontsize=10)
    
    fig.suptitle("Nominal vs Robustness (RD@k) Across Models and Languages", fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig("figures/nominal_vs_rd_all_models.png", dpi=300, bbox_inches="tight")
    plt.close()
    
def show_24_plots(models, model_names):
    languages = ["Java", "C++", "JS"]
    perturbations = ["DocString", "Syntax", "Format", "FuncName"]
    colors = ["#0072B2", "#D55E00", "#009E73"]  # one per language
    
    fig, axes = plt.subplots(6, 4, figsize=(16, 18), sharex=True, sharey=True)
    plt.subplots_adjust(hspace=0.4, wspace=0.25)
    
    for row, (model_data, model_name) in enumerate(zip(models, model_names)):
        for col, pert in enumerate(perturbations):
            ax = axes[row, col]
    
            for lang_data, lang_label, color in zip(model_data, languages, colors):
                nominal = lang_data["nominal"]
                rd_val = lang_data[pert][1]  # RD@k
                ax.scatter(nominal, rd_val, color=color, label=lang_label, s=60)
                ax.text(nominal + 0.005, rd_val, lang_label, fontsize=7)
    
            # Diagonal line for reference
            ax.plot([0, 1], [0, 1], "k--", alpha=0.3)
    
            # Labels and formatting
            if row == 0:
                ax.set_title(pert, fontsize=12, fontweight="bold")
            if col == 0:
                ax.set_ylabel(model_name, fontsize=11, fontweight="bold")
    
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.grid(alpha=0.3)
    
    # Common X/Y labels
    fig.text(0.5, 0.04, "Nominal", ha="center", fontsize=12, fontweight="bold")
    fig.text(0.04, 0.5, "RD@k", va="center", rotation="vertical", fontsize=12, fontweight="bold")
    
    # Shared legend for languages
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, label=l, markersize=8)
               for c, l in zip(colors, languages)]
    fig.legend(handles=handles, loc='lower center', ncol=3, fontsize=10, frameon=False)
    
    fig.suptitle("Nominal vs Robustness (RD@k) Across Models, Perturbations, and Languages", fontsize=14, y=0.995)
    plt.tight_layout(rect=[0.05, 0.05, 1, 0.97])
    
    # Save to file
    plt.savefig("nominal_vs_rd_6models_4perturbations.png", dpi=300, bbox_inches="tight")
    plt.close()

show_24_plots(models, model_names)
