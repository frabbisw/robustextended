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

# evalplus_dir = "evalplus_all"
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

def test_java(solution, org_sol, main, new_entry_point, old_entry_point):
    solution = org_sol
    solution = solution.replace("Solution", "SolutionGenerated")

    with open(f"../{testing_folder}/Main.java", "w") as f:
        f.write(main)
    with open(f"../{testing_folder}/Solution.java", "w") as f:
        f.write(org_sol)
    with open(f"../{testing_folder}/SolutionGenerated.java", "w") as f:
        f.write(solution)
    os.chdir(f"../{testing_folder}/")
    try:
        compilation_output = subprocess.run(['javac', 'Main.java', 'Solution.java', 'SolutionGenerated.java'], timeout=20, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            print(str(compilation_output.stderr).lower())
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=4, capture_output=True)
        try:
            subprocess.run(['rm', f'../{testing_folder}/Solution.class', f'../{testing_folder}/SolutionGenerated.class', f'../{testing_folder}/Main.class'], capture_output=False)

        except:
            None
        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif len(output.stderr) > 10:
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]

testing_folder = "testing_dir"
evalplus_dir = "/home/frabbi/Desktop/evalplus_all"

generated_path = f"../datasets/codegen6bmulti/generated_pass5_1/java/nominal/f_s0.jsonl"
lang = "java"
generated_data = load_prompts(generated_path)
nominal_data = get_nominal_prompts(lang)

generated_data.sort(key=lambda x: x["task_id"])
nominal_data.sort(key=lambda x: x["task_id"])

failed_list = []
from tqdm import tqdm as tq
for i in tq(range(164)):
    # if generated_data[i]["task_id"] in ["Java/32", "Java/87"]:
    #     continue
    assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
    main_method = get_evalplus_main_class_for_java(generated_data[i]["task_id"])
    solution_class = get_evalplus_slution_for_java(generated_data[i]["task_id"])
    passed_status, run_status = test_java(solution_class, solution_class, main_method, generated_data[i]["entry_point"], generated_data[i]["entry_point"])

    if passed_status == 0:
        failed_list.append(generated_data[i]["task_id"])

print(failed_list)