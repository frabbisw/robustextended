import collections
import json
import pdb
import pickle
import random

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
            prompts.append(json.loads(line)["prompt"]+json.loads(line)["canonical_solution"])
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

def get_nominal_dict(lang, type):
    assert type in ["nominal", "partial"]
    if type == "nominal":
        prompts = load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")
    else:
        prompts = load_prompts(f"../datasets/nominal/humaneval{lang}_partial.jsonl")
    nd = {}
    for p in prompts:
        nd[p["task_id"]] = p["prompt"]
    return nd

# def test_directory(directory, lang):
#     file_paths = [f for f in listdir(directory) if isfile(join(directory, f))]
#     for file_name in file_paths:
#         file_path = join(directory, file_name)
#         print(file_path)
#         generated_data = test_file(file_path, lang)
#         save_prompts(file_path, generated_data)

langs = ["js","java","cpp"]
# models = ["incoder1b", "codegen6bmulti"]
models = ["codegen2bmulti"]
nominals = ["nominal", "partial"]
methods = ["nlaugmenter", "natgen", "format", "func_name"]


def load_perturbed_prompts_for_samples(aug_method_path, aug_method_name, method_name, lang):
    if method_name in ["natgen","format"]:
        nominals = get_nominal_dict(lang, "partial")
    else:
        nominals = get_nominal_dict(lang, "nominal")

    prompts = []
    with open(aug_method_path, encoding="utf8") as f:
        for line in f.readlines():
            v = json.loads(line)
            prompts.append({"task_id":v["task_id"], "perturbed_prompt":v["prompt"], "nominal_prompt": nominals[v["task_id"]],  "aug_method_name":aug_method_name, "method_name": method_name, "naturalness_nominal": -1, "naturalness_perturbed": -1, "semantic": -1})
    return prompts

def get_100_samples(lang):
    datasets_path = f"../datasets/perturbed/humaneval{lang}/full"
    samples = []
    for method in methods:
        method_path = os.path.join(datasets_path, method)
        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            aug_method_name = aug_method_path[aug_method_path.rfind(f"humaneval{lang}")+len(f"humaneval{lang}")+1:aug_method_path.rfind("_")]
            samples += load_perturbed_prompts_for_samples(aug_method_path, aug_method_name, method, lang)

    random.seed(1223)
    random.shuffle(samples)
    id = 0
    for s in samples:
        s["unique_id"] = f"{lang}#{id}"
        id += 1
    # random.shuffle(samples)



    return samples[:100]

# def create_str_samples(lang):
#     datasets_path = f"../datasets/perturbed/humaneval{lang}/full"
#     samples = get_100_samples(lang, datasets_path)
#     return samples
    # print(samples)

java_samples = get_100_samples("java")

# print(java_samples)
# exit()

cpp_samples = get_100_samples("cpp")
js_samples = get_100_samples("js")



with open("../datasets/humaneval_samples/java_samples.json", "w", encoding='utf-8') as f:
    json.dump(java_samples, f, ensure_ascii=False, indent=2)
    print(len(java_samples))
print("java_samples ready")
with open("../datasets/humaneval_samples/cpp_samples.json", "w", encoding='utf-8') as f:
    json.dump(cpp_samples, f, ensure_ascii=False, indent=2)
    print(len(cpp_samples))
print("cpp_samples ready")
with open("../datasets/humaneval_samples/js_samples.json", "w", encoding='utf-8') as f:
    json.dump(js_samples, f, ensure_ascii=False, indent=2)
    print(len(js_samples))
print("js_samples ready")