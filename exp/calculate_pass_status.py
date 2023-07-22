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
def get_nominal_prompts(lang):
    return load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")


def get_evalplus_test_cases(task_id, lang):
    with open(join(join(join(evalplus_dir, lang)), task_id.replace("/", ""), f"main.{lang}"), "r") as f:
        return f.read()
def get_evalplus_solution(task_id, lang):
    with open(join(join(join(evalplus_dir,lang)),task_id.replace("/",""),f"solution.{lang}"), "r") as f:
        return f.read()
def get_evalplus_main_class_for_java(task_id):
    with open(join(join(join(evalplus_dir,"java")),task_id.replace("/",""),f"Main.java"), "r") as f:
        return f.read()
def get_evalplus_slution_for_java(task_id):
    with open(join(join(join(evalplus_dir,"java")),task_id.replace("/",""),f"Solution.java"), "r") as f:
        return f.read()
java_imports = "import java.util.ArrayList;\n" \
           "import java.util.Arrays;\n" \
           "import java.util.List;\n" \
           "import java.util.Objects;\n" \
           "import java.util.Map;\n" \
           "import java.util.Random;\n" \
           "import java.util.HashMap;\n" \
           "import java.util.Optional;\n" \
           "import java.security.NoSuchAlgorithmException;\n"
def filter_java_solution(code, prompt, old_entry_point, new_entry_point):
    start_signs = ["<|endoftext|>", "<code>" ]
    end_signs = ["public class", "class Solution", "<|endoftext|>", "</code>" ]
    if old_entry_point not in ["makePalindrome", "decodeCyclic", "decodeShift", "findZero"]:
        code = code.replace(new_entry_point, old_entry_point)
    prompt_start = code.find(prompt)
    if prompt_start < 0:
        for sign in start_signs:
            sign_pos = code.find(sign)
            if 20 > sign_pos > prompt_start:
                prompt_start = sign_pos + len(sign)
        prompt_start = max(prompt_start, 0)

    prompt_end = prompt_start+len(prompt)
    for sign in end_signs:
        code_end = code.find(sign, prompt_end)
        if code_end >= 0:
            code = code[prompt_start: code_end]
    return code, code.replace("Solution", "SolutionGenerated")

def test_java_he(solution, main):
    with open(f"../{testing_folder}/Main.java", "w") as f:
        f.write(main)
    with open(f"../{testing_folder}/Solution.java", "w") as f:
        f.write(solution)
    os.chdir(f"../{testing_folder}/")

    try:
        if os.path.exists(f'../{testing_folder}/Solution.class'):
            subprocess.run(['rm', f'../{testing_folder}/Solution.class'], capture_output=False)
        if os.path.exists(f'../{testing_folder}/Main.class'):
            subprocess.run(['rm', f'../{testing_folder}/Main.class'], capture_output=False)
    except Exception as e:
        print(e[:100])

    try:
        compilation_output = subprocess.run(['javac', 'Main.java', 'Solution.java'], timeout=20, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            # print(str(compilation_output.stderr).lower()[:100])
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            # print(str(output.stderr))
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "exception" in str(output.stderr).lower() or "error" in str(output.stderr).lower():
            # print(str(output.stderr))
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            # print("passed")
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        # print(e)
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]

def test_java_ep(solution_generated, org_solution, main):
    with open(f"../{testing_folder}/Main.java", "w") as f:
        f.write(main)
    with open(f"../{testing_folder}/Solution.java", "w") as f:
        f.write(org_solution)
    with open(f"../{testing_folder}/SolutionGenerated.java", "w") as f:
        f.write(solution_generated)
    os.chdir(f"../{testing_folder}/")

    try:
        if os.path.exists(f'../{testing_folder}/Solution.class'):
            subprocess.run(['rm', f'../{testing_folder}/Solution.class'], capture_output=False)
        if os.path.exists(f'../{testing_folder}/SolutionGenerated.class'):
            subprocess.run(['rm', f'../{testing_folder}/SolutionGenerated.class'], capture_output=False)
        if os.path.exists(f'../{testing_folder}/Main.class'):
            subprocess.run(['rm', f'../{testing_folder}/Main.class'], capture_output=False)
    except Exception as e:
        print(e[:100])

    try:
        compilation_output = subprocess.run(['javac', 'Solution.java', 'SolutionGenerated.java', 'Main.java'], timeout=20, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            # print(str(compilation_output.stderr).lower()[:100])
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            # print(str(output.stderr))
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "exception" in str(output.stderr).lower() or "error" in str(output.stderr).lower():
            # print(str(output.stderr))
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            # print("passed")
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        # print(e)
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]


def filter_js_cpp_solution(code, prompt, old_entry_point, new_entry_point):
    start_signs = ["<|endoftext|>", "<code>" ]
    end_signs = ["<|endoftext|>", "</code>" , "/*", "#include", "int main()", f"const {new_entry_point}", f"const {old_entry_point}", "console.log("]
    if old_entry_point not in ["makePalindrome", "decodeCyclic", "decodeShift", "findZero", "make_palindrome", "decode_cyclic", "decode_shift", "find_zero"]:
        code = code.replace(new_entry_point, old_entry_point)
    prompt_start = code.find(prompt)
    if prompt_start < 0:
        for sign in start_signs:
            sign_pos = code.find(sign)
            if 20 > sign_pos > prompt_start:
                prompt_start = sign_pos + len(sign)
        prompt_start = max(prompt_start, 0)

    prompt_end = prompt_start+len(prompt)
    for sign in end_signs:
        code_end = code.find(sign, prompt_end)
        if code_end >= 0:
            code = code[prompt_start: code_end]
    return code, code.replace(old_entry_point, "generatedMethodName")
# def test_js_he(solution, main):

def test_js_he(solution, main):
    full_code = solution + main
    with open(f"../{testing_folder}/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir(f"../{testing_folder}/")
    try:
        output = subprocess.run(['node', 'Sample.js'], timeout=8, capture_output=True)
        # print(full_code)
        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "error" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]

def test_js_ep(solution_generated, main):
    full_code = main.replace("###GENERATEDCODE###", solution_generated)
    with open(f"../{testing_folder}/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir(f"../{testing_folder}/")
    try:
        output = subprocess.run(['node', 'Sample.js'], timeout=8, capture_output=True)
        # print(full_code)
        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "error" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
def test_cpp_he(solution, main):
    full_code = solution + main
    with open(f"../{testing_folder}/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir(f"../{testing_folder}/")

    try:
        if os.path.exists(f'../{testing_folder}/cpp_code'):
            subprocess.run(['rm', f'../{testing_folder}/cpp_code'], capture_output=False)
    except Exception as e:
        print(e)
    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=30,capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "segmentation fault" in str(output.stderr).lower() or "error" in str(
                output.stderr).lower() or "terminate" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]

def test_cpp_ep(solution_generated, main):
    full_code = main.replace("###GENERATEDCODE###", solution_generated)
    with open(f"../{testing_folder}/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir(f"../{testing_folder}/")
    try:
        if os.path.exists(f'../{testing_folder}/cpp_code'):
            subprocess.run(['rm', f'../{testing_folder}/cpp_code'], capture_output=False)
    except Exception as e:
        print(e)
    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=30,
                                            capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "segmentation fault" in str(output.stderr).lower() or "error" in str(
                output.stderr).lower() or "terminate" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
def test_file(generated_path, lang):
    generated_data = load_prompts(generated_path)
    nominal_data = get_nominal_prompts(lang)

    generated_data.sort(key=lambda x: x["task_id"])
    nominal_data.sort(key=lambda x: x["task_id"])

    result = {}
    for i in range(164):
        assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
        if lang == "cpp":
            test_he = generated_data[i]["test"]
            test_ep = get_evalplus_test_cases(generated_data[i]["task_id"], lang)
            solution_gc_he, solution_gc_ep = filter_js_cpp_solution(generated_data[i]["gc"],generated_data[i]["prompt"],nominal_data[i]["entry_point"],generated_data[i]["entry_point"])

            passed_status_he, run_status_he = test_cpp_he(solution_gc_he, test_he)
            passed_status_ep, run_status_ep = test_cpp_ep(solution_gc_ep, test_ep)
            # print(generated_data[i]["task_id"], passed_status_he, passed_status_ep)

        elif lang == "java":
            test_he = java_imports + generated_data[i]["test"]
            test_ep = get_evalplus_main_class_for_java(generated_data[i]["task_id"])
            solution_gc_he, solution_gc_ep = filter_java_solution(generated_data[i]["gc"], generated_data[i]["prompt"], nominal_data[i]["entry_point"], generated_data[i]["entry_point"])
            solution_org = get_evalplus_slution_for_java(generated_data[i]["task_id"])

            passed_status_he, run_status_he = test_java_he(solution_gc_he, test_he)
            passed_status_ep, run_status_ep = test_java_ep(solution_gc_ep, solution_org, test_ep)

            # print(generated_data[i]["task_id"], passed_status_he, passed_status_ep)
        elif lang == "js":
            test_he = generated_data[i]["test"]
            test_ep = get_evalplus_test_cases(generated_data[i]["task_id"], lang)
            solution_gc_he, solution_gc_ep = filter_js_cpp_solution(generated_data[i]["gc"],generated_data[i]["prompt"],nominal_data[i]["entry_point"],generated_data[i]["entry_point"])

            passed_status_he, run_status_he = test_js_he(solution_gc_he, test_he)
            passed_status_ep, run_status_ep = test_js_ep(solution_gc_ep, test_ep)
            # print(generated_data[i]["task_id"], passed_status_he, passed_status_ep)
        generated_data[i]["passed_he"] = passed_status_he
        generated_data[i]["run_status_he"] = run_status_he
        generated_data[i]["passed_ep"] = passed_status_ep
        generated_data[i]["run_status_ep"] = run_status_ep
    return generated_data

def test_aug_method(directory, lang):
    print(directory)
    file_paths = [f for f in listdir(directory) if isfile(join(directory, f))]
    for file_name in file_paths:
        file_path = join(directory, file_name)
        # print(file_path)
        generated_data = test_file(file_path, lang)
        save_prompts(file_path, generated_data)

def test_lang(lang, datasets_path):
    lang_path = os.path.join(datasets_path, lang)
    for method in nominals:
        method_path = os.path.join(lang_path, method)
        # print(method_path)
        test_aug_method(method_path, lang)

    for method in methods:
        method_path = os.path.join(lang_path, method)
        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            test_aug_method(aug_method_path, lang)

evalplus_dir = "/home/frabbi/Desktop/evalplus_all"

nominals = ["nominal", "partial"]
methods = ["nlaugmenter", "natgen", "format", "func_name"]

model_name = sys.argv[1]
lang_name = sys.argv[2]
testing_folder = f"testing_dir{sys.argv[3]}"
print(model_name, lang_name)

datasets_path = f"../datasets/{model_name}/generated_pass5_1"
test_lang(lang_name, datasets_path)
