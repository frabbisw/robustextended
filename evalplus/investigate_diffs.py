import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import ast
import re
from collections import Counter

import difflib

def diff_strings(string1, string2):
    diff = difflib.ndiff(string1.splitlines(), string2.splitlines())
    return '\n'.join(diff)

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

evalplus_type = "full"
evalplus_prompts = load_prompts(f"/home/frabbi/Documents/evalplus/{evalplus_type}.jsonl")
humaneval_prompts = load_prompts(f"../dataset-release/nominal/HumanEval.jsonl")

evalplus_dict = {}
for prompt in evalplus_prompts:
    evalplus_dict[prompt['task_id']]=prompt
humaneval_dict = {}
for prompt in humaneval_prompts:
    humaneval_dict[prompt['task_id']]=prompt

out = ""
for task_id in evalplus_dict.keys():
    evalplus_solution = evalplus_dict[task_id]['prompt']+evalplus_dict[task_id]['canonical_solution']
    humaneval_solution = humaneval_dict[task_id]['prompt']+humaneval_dict[task_id]['canonical_solution']
    df = diff_strings(evalplus_dict[task_id]['canonical_solution'], humaneval_dict[task_id]['canonical_solution'])
    out += task_id + "\n"
    out += df + "\n"
    out += "*"*50 + "\n"
