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

java_nominals = load_prompts("../datasets/nominal/humanevaljava_nominal_f_s0.jsonl")
cpp_nominals = load_prompts("../datasets/nominal/humanevalcpp_nominal_f_s0.jsonl")
js_nominals = load_prompts("../datasets/nominal/humanevaljs_nominal_f_s0.jsonl")

java_solutions = load_solutions("/home/frabbi/Desktop/evalplusmodified", "java")
cpp_solutions = load_solutions("/home/frabbi/Desktop/evalplusmodified", "cpp")
js_solutions = load_solutions("/home/frabbi/Desktop/evalplusmodified", "js")

solutions = {"java":java_solutions, "cpp":cpp_solutions, "js":js_solutions}
nominals = {"java":java_nominals, "cpp":cpp_nominals, "js":js_nominals}


def divide_solution(solution, entry_point):
    if entry_point == "for":
        print("baal")
        exit()
    method_line = solution.find("\n", solution.find(entry_point, solution.find("*/")))
    return solution[:method_line+1], solution[method_line+1:]

    # method_sign = {"java":f"public class {entry_point}","js":f"const {entry_point}","cpp":f"{entry_point}("}

for lang in ["java","cpp","js"]:
    print(solutions[lang].keys())
    for task_id in solutions[lang].keys():
        # old_solution = partials[lang][task_id]['prompt']+partials[lang][task_id]['canonical_solution']
        # old_prompt = partials[lang][task_id]['canonical_solution']
        new_solution = solutions[lang][task_id]
        entry_point = nominals[lang][task_id]['entry_point']
        if entry_point == "for":
            nominals[lang][task_id]['entry_point'] = {"java":"findZero","js":"findZero","cpp":"find_zero"}[lang]
            entry_point = nominals[lang][task_id]['entry_point']
        prompt, canonical_solution = divide_solution(new_solution, entry_point)

        assert len(prompt) > 10
        assert len(canonical_solution) > 10

        nominals[lang][task_id]['prompt'] = prompt
        nominals[lang][task_id]['canonical_solution'] = canonical_solution

# save_prompts("../datasets/nominal/HumanEval_java.jsonl", nominals["java"])
# save_prompts("../datasets/nominal/HumanEval_cpp.jsonl", nominals["cpp"])
# save_prompts("../datasets/nominal/HumanEval_js.jsonl", nominals["js"])


