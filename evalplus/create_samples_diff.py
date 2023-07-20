import json
import os
import jsonlines
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

solution_file_names = {"js":"solution.js", "cpp":"solution.cpp","java":"Solution.java"}
task_lang_names = {"js":"JavaScript", "cpp":"CPP","java":"Java"}

def load_solutions(directory, lang):
    solutions = {}
    lang_path = os.path.join(directory,lang)
    for root, folders, files in os.walk(lang_path):
        for folder in folders:
            task_path = os.path.join(lang_path, folder)
            solution_path = os.path.join(task_path, solution_file_names[lang])
            task_id = folder.replace(task_lang_names[lang],f"{task_lang_names[lang]}/")
            with open(solution_path, "r") as f:
                solutions[task_id] = f.read()
    return solutions


evalplus_type = "full"
with open(f"java_inputs_{evalplus_type}", "rb") as f:
    java_inputs = pickle.load(f)
with open(f"cpp_inputs_{evalplus_type}", "rb") as f:
    cpp_inputs = pickle.load(f)
with open(f"js_inputs_{evalplus_type}", "rb") as f:
    js_inputs = pickle.load(f)

def diff_strings(string1, string2):
    diff = difflib.ndiff(string1.splitlines(), string2.splitlines())
    return '\n'.join(diff)

java_partials = load_prompts("../datasets/nominal/humanevaljava_partial_f_s0.jsonl")
cpp_partials = load_prompts("../datasets/nominal/humanevalcpp_partial_f_s0.jsonl")
js_partials = load_prompts("../datasets/nominal/humanevaljs_partial_f_s0.jsonl")

java_solutions = load_solutions("/home/frabbi/Desktop/evalplusdata", "java")
cpp_solutions = load_solutions("/home/frabbi/Desktop/evalplusdata", "cpp")
js_solutions = load_solutions("/home/frabbi/Desktop/evalplusdata", "js")

solutions = {"java":java_solutions, "cpp":cpp_solutions, "js":js_solutions}
partials = {"java":java_partials, "cpp":cpp_partials, "js":js_partials}



for lang in ["java","cpp","js"]:
    contents = ""
    for task_id in solutions[lang].keys():
        old_solution = partials[lang][task_id]['prompt']+partials[lang][task_id]['canonical_solution']
        old_prompt = partials[lang][task_id]['canonical_solution']
        new_solution = solutions[lang][task_id]
        df = diff_strings(old_solution, new_solution)
        contents += f"\n{'-'*50}\nTask ID: {task_id}\n{'-'*50}\nOld Solution:\n{'-'*50}\n{old_solution}\n{'-'*50}\nNew Solution:\n{'-'*50}\n{new_solution}\n{'-'*50}\nDiff:\n{'-'*50}\n{df}\n{'='*50}\n\n"

    with open(f"diff{lang}.{lang}", "w") as f:
        f.write(contents)