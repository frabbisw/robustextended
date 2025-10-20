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
        
lang = sys.argv[1]
model_name = "magicoder7b"
pert_type = "nlaugmenter"

nominal_map = get_nominal_map(lang, "nominal", model_name)

# print(nominal_map[pert_prompts[i]["CPP/99"]])

# exit(0)

stat = {}
for aug_type in os.listdir(f"{DATASET_PATH}/{model_name}/generated_pass5_1/{lang}/{pert_type}"):
    stat[aug_type] = {"nominal": 0, "perturbed": 0, "fixed": 0}
    for ind in range(5):
        aug_filepath = f"{DATASET_PATH}/{model_name}/backup/{lang}/{pert_type}/{aug_type}/f_s{ind}.jsonl"
        pert_prompts = load_prompts(aug_filepath)
        for j, p in enumerate(pert_prompts):            
            try:
                stat[aug_type]["nominal"] += int(nominal_map[pert_prompts[j]["task_id"]]["passed_evalplus"])
                stat[aug_type]["perturbed"] += int(pert_prompts[j]["passed_evalplus"])
                stat[aug_type]["fixed"] += int(pert_prompts[j]["passed_evalplus_processed"])
            except:
                print(aug_filepath)
                exit(0)
    


def show_plot(data, lang):
    print(data)
    # Prepare data
    perturbations = list(data.keys())
    x = np.arange(len(perturbations))
    width = 0.25
    total = 164 * 5
    
    nominal_pct = [data[k]['nominal'] / total * 100 for k in perturbations]
    perturbed_pct = [data[k]['perturbed'] / total * 100 for k in perturbations]
    fixed_pct = [data[k]['fixed'] / total * 100 for k in perturbations]
    
    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.bar(x - width, nominal_pct, width, label='Nominal', color='#8172b2')
    ax.bar(x, perturbed_pct, width, label='Perturbed', color='#4c72b0')
    ax.bar(x + width, fixed_pct, width, label='Fixed', color='#55a868')
    
    # Customize
    ax.set_ylabel('Pass3@5 (%)')
    # ax.set_title('Pass Rate Comparison: Nominal vs Perturbed vs Fixed Prompts')
    ax.set_xticks(x)
    ax.set_xticklabels(perturbations, rotation=45, ha='right')
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.legend()
    fig.tight_layout()
    
    # Save as high-resolution figure
    plt.savefig(f"figures/{lang}.png", dpi=300, bbox_inches='tight')

show_plot(stat, lang)
