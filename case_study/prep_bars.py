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
    for i in range(5):
        aug_filepath = f"{DATASET_PATH}/{model_name}/backup/{lang}/{pert_type}/{aug_type}/f_s{i}.jsonl"
        pert_prompts = load_prompts(aug_filepath)
        for i, p in enumerate(pert_prompts):
            stat[aug_type]["nominal"] += int(nominal_map[pert_prompts[i]["task_id"]]["passed_evalplus"])
            stat[aug_type]["perturbed"] += int(pert_prompts[i]["passed_evalplus"])
            stat[aug_type]["perturbed"] += int(pert_prompts[i]["passed_evalplus_processed"])
        



print(stat)
