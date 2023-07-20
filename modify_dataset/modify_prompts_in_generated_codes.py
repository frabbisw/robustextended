import json
import os
import jsonlines
import pathlib
from tqdm import tqdm as tq
import sys
import pickle
import subprocess
import re
import time
import difflib

def load_prompts(filename):
    prompts = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            prompts[prompt['task_id']]=prompt
    return prompts
def save_prompts(filename, prompts):
    if isinstance(prompts, list):
        with jsonlines.open(filename, mode='w') as writer:
            for line in prompts:
                jsonlines.Writer.write(writer, line)
    elif isinstance(prompts, dict):
        tmp = []
        for task_id in prompts.keys():
            tmp.append(prompts[task_id])
        # print(tmp)
        with jsonlines.open(filename, mode='w') as writer:
            for line in tmp:
                jsonlines.Writer.write(writer, line)

modified_cpp_prompts = load_prompts("../datasets/nominal/humanevalcpp_partial.jsonl")
modified_js_prompts = load_prompts("../datasets/nominal/humanevaljs_partial.jsonl")
modified_java_prompts = load_prompts("../datasets/nominal/humanevaljava_partial.jsonl")
modified_prompts = {"java":modified_java_prompts, "cpp": modified_cpp_prompts, "js": modified_js_prompts}


models = ["codegen2bmulti", "codegen6bmulti", "incoder1b", "incoder6b"]
langs = ["cpp", "java", "js"]
partial_names = ["partial","natgen","format"]


for i in tq(range(len(models))):
    model = models[i]
    for lang in langs:
        src_prompts = modified_prompts[lang]
        for name in partial_names:
            target_root = f"../datasets/{model}/generated_pass5_1/{lang}/{name}"
            for target_filepath in list(pathlib.Path(target_root).rglob("*")):
                if os.path.isfile(target_filepath):
                    print(target_filepath)
                    target_prompts = load_prompts(target_filepath)
                    try:
                        for task_id in src_prompts.keys():
                            target_prompts[task_id]["prompt"] = src_prompts[task_id]["prompt"]
                            target_prompts[task_id]["canonical_solution"] = src_prompts[task_id]["canonical_solution"]
                            target_prompts[task_id]["entry_point"] = src_prompts[task_id]["entry_point"]
                            save_prompts(target_filepath, target_prompts)
                    except:
                        print(target_filepath, "*"*10)
                        continue
