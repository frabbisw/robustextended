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

CODE_RUN_STATUS = {"PASSED":0, "ASSERTION":1, "COMPILATION":2, "TIMEOUT": 3}

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


def test_java(solution, main, new_entry_point, old_entry_point):
    solution = solution[:solution.find("<|endoftext|>")]
    solution=eliminate_second_Sollution(solution)

    main = main.replace(old_entry_point, new_entry_point)

    main = "import java.util.ArrayList;\n" \
           "import java.util.Arrays;\n" \
           "import java.util.List;\n" \
           "import java.util.Objects;\n" \
           "import java.util.Map;\n" \
           "import java.util.Random;\n" \
           "import java.util.HashMap;\n" \
           "import java.util.Optional;\n" \
           "import java.security.NoSuchAlgorithmException;\n" \
           + main
    with open("../tmp/Main.java", "w") as f:
        f.write(main)
    with open("../tmp/Solution.java", "w") as f:
        f.write(solution)
    os.chdir("../tmp/")
    try:
        subprocess.check_output(['javac', 'Main.java', 'Solution.java'], stderr=subprocess.STDOUT)
        subprocess.check_output(['java', 'Main'], stderr=subprocess.STDOUT, timeout=3)
        return 1, CODE_RUN_STATUS["PASSED"]
    except subprocess.CalledProcessError as e:
        if "assertion" in e.output.decode('utf-8').lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]

def test_cpp(code, main, new_entry_point, old_entry_point):
    if "<|endoftext|>" in code:
        code = code[:code.find("<|endoftext|>")]
    if "int main()" in code:
        code = code[:code.find("int main()")]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main
    with open("../tmp/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")

    try:
        subprocess.check_output(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], stderr=subprocess.STDOUT)
        subprocess.check_output(['./cpp_code'], stderr=subprocess.STDOUT, timeout=3)
        return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        if "assertion" in e.output.decode('utf-8').lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]

def test_js(code, main, new_entry_point, old_entry_point):
    code = code[:code.find("<|endoftext|>")]
    cmnt_index = code.find("/*")
    cmnt_index = code.find("/*", cmnt_index + 5)
    if cmnt_index > 0:
        code = code[:cmnt_index]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main

    with open("../tmp/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")
    try:
        subprocess.check_output(['node', 'Sample.js'], stderr=subprocess.STDOUT, timeout=3)
        return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        if "assertion" in e.output.decode('utf-8').lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]

def test_file(generated_path, lang):
    generated_data = load_prompts(generated_path)
    nominal_data =  get_nominal_prompts(lang)

    generated_data.sort(key=lambda x: x["task_id"])
    nominal_data.sort(key=lambda x: x["task_id"])

    result = {}
    for i in range(164):
        if lang == "cpp":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_cpp(generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        elif lang == "java":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_java(generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        elif lang == "js":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_js(generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        generated_data[i]["passed"] = passed_status
        generated_data[i]["run_status"] = run_status
    return generated_data
def test_directory(directory, lang):
    file_paths = [f for f in listdir(directory) if isfile(join(directory, f))]
    for file_name in file_paths:
        file_path = join(directory, file_name)
        print(file_path)
        generated_data = test_file(file_path, lang)
        save_prompts(file_path, generated_data)

# nominal_prompts = load_prompts("../datasets/nominal/HumanEval_cpp.jsonl")
# nominal_prompts.sort(key=lambda x: x["task_id"])

def get_nominal_prompts(lang):
    return load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")

# methods = []
# nominals = ["nominal"]
def test_lang(lang):
    lang_path = os.path.join(datasets_path, lang)
    for method in nominals:
        method_path = os.path.join(lang_path, method)
        print(method_path)
        test_directory(method_path, lang)

    for method in methods:
        method_path = os.path.join(lang_path, method)
        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            print(aug_method_path)
            test_directory(aug_method_path, lang)

langs = ["js","java","cpp"]
models = ["incoder1b", "codegen6bmulti"]
nominals = ["nominal", "partial"]
methods = ["nlaugmenter", "natgen", "format", "func_name"]

for model in models:
    for lang in langs:
        datasets_path = f"../datasets/{model}/generated_pass5_1"
        test_lang(lang)