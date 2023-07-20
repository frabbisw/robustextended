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

def test_cpp(code, main, entry_point):
    code = code.replace("usingnamespace", "using namespace")
    code = code.replace("using std;", "using namespace std;")

    start_index = code.find("<|endoftext|>")
    if start_index < 0:
        start_index = 0
    elif start_index < 5:
        start_index = start_index + len("<|endoftext|>")
    else:
        start_index = 0
    end_index = code.rfind("<|endoftext|>")
    if end_index < 5:
        end_index = len(code)

    code = code[start_index:end_index]

    if f"</code>" in code:
        code = code[:code.find("</code>")]
    if f"<code>" in code:
        code = code[code.find("<code>"):]

    cmnt_index = code.find("/*")
    cmnt_index = code.find("/*", cmnt_index + 5)
    if cmnt_index > 0:
        code = code[:cmnt_index]
    if "int main()" in code:
        code = code[:code.find("int main()")]

    if len(entry_point) < 5:
        code = code.replace(f"{entry_point}(", "generatedMethodName(")
    else:
        code = code.replace(entry_point, "generatedMethodName")
    main = main.replace("###GENERATEDCODE###", code)

    # print(code)
    # print(main)

    with open(f"../{testing_folder}/cpp_code.cpp", "w") as f:
        f.write(main)
    os.chdir(f"../{testing_folder}/")

    try:
        if os.path.exists(f'../{testing_folder}/cpp_code'):
            subprocess.run(['rm', f'../{testing_folder}/cpp_code'], capture_output=False)
    except:
        None

    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=60, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            print("error inside call in try", str(compilation_output.stderr).lower()[:500])
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            print("assertion")
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "segmentation fault" in str(output.stderr).lower() or "error" in str(output.stderr).lower() or "terminate" in str(output.stderr).lower():
            print("runtime", str(output.stderr).lower())
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print("subprocess.CalledProcessError", str(compilation_output.stderr).lower()[:100])
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        print("timeout")
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print("extra",str(e).lower()[:100])
        return 0, CODE_RUN_STATUS["COMPILATION"]


testing_folder = "testing_dir"
evalplus_dir = "/home/frabbi/Desktop/evalplus_all"

generated_path = f"../datasets/codegen6bmulti/generated_pass5_1/cpp/nominal/f_s0.jsonl"
lang = "cpp"
generated_data = load_prompts(generated_path)
nominal_data = get_nominal_prompts(lang)

generated_data.sort(key=lambda x: x["task_id"])
nominal_data.sort(key=lambda x: x["task_id"])

failed_list = []
from tqdm import tqdm as tq
for i in tq(range(164)):
    if generated_data[i]["task_id"] == "CPP/32":
        generated_data[i]["entry_point"] = "find_zero"
    assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]

    if generated_data[i]["task_id"] not in ['CPP/137', 'CPP/15', 'CPP/163', 'CPP/18', 'CPP/32', 'CPP/39', 'CPP/44', 'CPP/46', 'CPP/49', 'CPP/50', 'CPP/55', 'CPP/58', 'CPP/63', 'CPP/76', 'CPP/95']:
        continue

    main_method = get_evalplus_test_cases(lang, generated_data[i]["task_id"])
    print(nominal_data[i]["task_id"])
    passed_status, run_status = test_cpp(generated_data[i]["prompt"]+generated_data[i]["canonical_solution"], main_method, generated_data[i]["entry_point"])

    if passed_status == 0:
        failed_list.append(generated_data[i]["task_id"])

print(failed_list)