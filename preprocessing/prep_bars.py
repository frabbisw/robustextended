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
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3, "RUNTIME": 4}

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

DATASET_PATH = "/home/f_rabbi/recode/robustextended/datasets"

def get_nominal_map(lang, type, model_name):
    if type == "nominal":
        prompts = load_prompts(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/nominal/f_s0.jsonl")
    elif type == "partial":
        prompts = load_prompts(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/partial/f_s0.jsonl")
    
    return {p["task_id"]: p for p in prompts}
        
# lang = sys.argv[1]
model_name = "magicoder7b"
pert_type = "nlaugmenter"


# print(nominal_map[pert_prompts[i]["CPP/99"]])

# exit(0)

def get_stat(lang, model_name):
    nominal_map = get_nominal_map(lang, "nominal", model_name)
    stat = {}
    for aug_type in os.listdir(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/{pert_type}"):
        stat[aug_type] = {}
        for ind in range(5):
            aug_filepath = f"{DATASET_PATH}/{model_name}/backup/{lang}/{pert_type}/{aug_type}/f_s{ind}.jsonl"
            pert_prompts = load_prompts(aug_filepath)
            for j, p in enumerate(pert_prompts):            
                try:
                    if j not in stat[aug_type].keys():
                        stat[aug_type][j] = {"nominal": [], "perturbed": [], "fixed": []}
                        
                    stat[aug_type][j]["nominal"].append(int(nominal_map[pert_prompts[j]["task_id"]]["passed_evalplus"]))
                    stat[aug_type][j]["perturbed"].append(int(pert_prompts[j]["passed_evalplus"]))
                    stat[aug_type][j]["fixed"].append(int(pert_prompts[j]["passed_evalplus_processed"]))
                    # stat[aug_type][j]["newly_fixed"].append(int(pert_prompts[j]["passed_evalplus_processed"] > pert_prompts[j]["passed_evalplus"]))
                    # stat[aug_type][j]["already_fixed"].append(int(pert_prompts[j]["passed_evalplus_processed"] > pert_prompts[j]["passed_evalplus"]))
                    # stat[aug_type][j]["newly_failed"].append(int(pert_prompts[j]["passed_evalplus_processed"] < pert_prompts[j]["passed_evalplus"]))
                    
                except Exception as e:
                    print(e)
                    print(aug_filepath)
                    exit(0)
    return stat

def show_plot(stat, lang, K):
    # ------------------------------
    # Example: simplified data extraction from your logic
    # (ensure 'newly_fixed' and 'newly_failed' are computed properly in your actual loop)
    # ------------------------------
    data = {}
    for aug_type in stat.keys():
        data[aug_type] = {
            "nominal": 0, "perturbed": 0, "fixed": 0,
            "newly_fixed": 0, "already_fixed": 0,
            "newly_failed": 0, "still_passed": 0
        }
        for j in stat[aug_type].keys():
            passed_nominal = int(sum(stat[aug_type][j]["nominal"]) >= K)
            passed_perturbed = int(sum(stat[aug_type][j]["perturbed"]) >= K)
            passed_fixed = int(sum(stat[aug_type][j]["fixed"]) >= K)

            data[aug_type]["nominal"] += passed_nominal
            data[aug_type]["perturbed"] += passed_perturbed
            data[aug_type]["fixed"] += passed_fixed

            # transitions
            if passed_fixed and not passed_perturbed:
                data[aug_type]["newly_fixed"] += 1
            if passed_fixed and passed_perturbed:
                data[aug_type]["already_fixed"] += 1
            if passed_perturbed and not passed_fixed:
                data[aug_type]["newly_failed"] += 1
            if passed_perturbed and passed_fixed:
                data[aug_type]["still_passed"] += 1

    # ------------------------------
    # Plotting
    # ------------------------------
    perturbations = list(data.keys())
    x = np.arange(len(perturbations))
    width = 0.25
    total = 164

    nominal_pct = [data[k]['nominal'] / total * 100 for k in perturbations]
    perturbed_pct = [data[k]['perturbed'] / total * 100 for k in perturbations]
    fixed_pct = [data[k]['fixed'] / total * 100 for k in perturbations]

    # stacked components
    newly_fixed_pct = [data[k]['newly_fixed'] / total * 100 for k in perturbations]
    already_fixed_pct = [data[k]['already_fixed'] / total * 100 for k in perturbations]
    newly_failed_pct = [data[k]['newly_failed'] / total * 100 for k in perturbations]
    still_passed_pct = [data[k]['still_passed'] / total * 100 for k in perturbations]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Nominal (single color)
    rects1 = ax.bar(x - width, nominal_pct, width, label='Nominal', color='#8172b2')

    # Perturbed (stacked)
    rects2a = ax.bar(x, still_passed_pct, width, label='Perturbed: Passed→Passed', color='#4c72b0')
    rects2b = ax.bar(x, newly_failed_pct, width, bottom=still_passed_pct,
                     label='Perturbed: Passed→Failed', color='#dd8452')

    # Fixed (stacked)
    rects3a = ax.bar(x + width, already_fixed_pct, width, label='Fixed: Passed→Passed', color='#55a868')
    rects3b = ax.bar(x + width, newly_fixed_pct, width, bottom=already_fixed_pct,
                     label='Fixed: Failed→Passed', color='#c44e52')

    # Customize
    ax.set_ylabel(f'Pass@{K} (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(perturbations, rotation=45, ha='right')
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(PercentFormatter())

    # Combine legend to avoid duplicate labels
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), ncol=2, loc='upper right')

    fig.tight_layout()
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f"figures/{lang}_prep_bar.png", dpi=300, bbox_inches='tight')
    # plt.show()

show_plot(get_stat("cpp", model_name), "cpp", 5)
print("cpp done")
show_plot(get_stat("java", model_name), "java", 5)
print("java done")
show_plot(get_stat("js", model_name), "js", 5)
print("js done")
