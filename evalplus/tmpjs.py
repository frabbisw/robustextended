import json
import pdb
import pickle
# from tqdm import tqdm as tq
import os
import subprocess
import jsonlines
from collections import Counter
from os import listdir
from os.path import isfile, join
import sys


CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3, "RUNTIME": 4}

def get_nominal_prompts(lang):
    return load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")

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


def get_evalplus_test_cases(lang, task_id):
    with open(join(join(join(evalplus_dir,lang)),task_id.replace("/",""),f"main.{lang}"), "r") as f:
        return f.read()
def get_evalplus_main_class_for_java(task_id):
    with open(join(join(join(evalplus_dir,"java")),task_id.replace("/",""),f"Main.java"), "r") as f:
        return f.read()
def get_evalplus_slution_for_java(task_id):
    with open(join(join(join(evalplus_dir,"java")),task_id.replace("/",""),f"Solution.java"), "r") as f:
        return f.read()
def eliminate_second_Sollution(sample_java_solution):
    ##eliminate 2nd solution class
    first_class_pointer = sample_java_solution.find("class Solution")
    if first_class_pointer < 0:
        return sample_java_solution
    second_class_pointer = sample_java_solution.find("class Solution", first_class_pointer + 5)
    if second_class_pointer < 0:
        second_class_pointer = sample_java_solution.find("public class", first_class_pointer + 5)
    if second_class_pointer < 0:
        return sample_java_solution
    sample_java_solution = sample_java_solution[:second_class_pointer]
    return sample_java_solution[:sample_java_solution.rfind("}")+1]

def test_js(gc, main, entry_point):
    start_index = gc.find("<|endoftext|>")
    if start_index < 0:
        start_index = 0
    elif start_index < 5:
        start_index = start_index + len("<|endoftext|>")
    else:
        start_index = 0
    end_index = gc.rfind("<|endoftext|>")
    if end_index < 5:
        end_index = len(gc)

    gc = gc[start_index:end_index]
    # if "\n}" in gc:
    #     gc = gc[:1+gc.find("\n}")]

    if f"</code>" in gc:
        gc = gc[:gc.find("</code>")]
    if f"<code>" in gc:
        gc = gc[gc.find("<code>"):]

    cmnt_index = gc.find("/*")
    cmnt_index = gc.find("/*", cmnt_index + 5)
    if cmnt_index > 0:
        gc = gc[:cmnt_index]
    gc = gc.replace(" \\\n", "\n")

    if "//" in gc:
        if "/*" and "*/" not in gc:
            line_cmnt = gc.find(f"//", gc.find("const"))
            if line_cmnt > 0:
                gc = gc[:line_cmnt]
    if len(entry_point) < 3:
        gc = gc.replace(f"const {entry_point} =", "const generatedMethodName =")
    else:
        gc = gc.replace(entry_point, "generatedMethodName")
    main = main.replace("###GENERATEDCODE###", gc)

    with open(f"../{testing_folder}/Sample.js", "w") as f:
        f.write(main)
    os.chdir(f"../{testing_folder}/")
    try:
        # if task_id == "JavaScript/162":
        #     subprocess.run(['npm', ' install', 'ts-md5', '--save'], capture_output=True)
        output = subprocess.run(['node', 'Sample.js'], timeout=8, capture_output=True)
        # print(full_code)
        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "error" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]


testing_folder = "testing_dir"
evalplus_dir = "/home/frabbi/Desktop/evalplus_all"

generated_path = f"../datasets/codegen6bmulti/generated_pass5_1/js/nominal/f_s0.jsonl"
lang = "js"
generated_data = load_prompts(generated_path)
nominal_data = get_nominal_prompts(lang)

generated_data.sort(key=lambda x: x["task_id"])
nominal_data.sort(key=lambda x: x["task_id"])

failed_list = []
from tqdm import tqdm as tq
for i in tq(range(164)):
    assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]

    main_method = get_evalplus_test_cases(lang, generated_data[i]["task_id"])
    passed_status, run_status = test_js(generated_data[i]["prompt"]+generated_data[i]["canonical_solution"], main_method, generated_data[i]["entry_point"])

    if passed_status == 0:
        failed_list.append(generated_data[i]["task_id"])

print(failed_list)