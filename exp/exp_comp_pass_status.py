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
def get_evalplus_test_cases(lang, task_id):
    with open(join(join(join(evalplus_dir,lang)),task_id.replace("/",""),f"main.{lang}"), "r") as f:
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
    return code

def test_java_he(solution, main):
    print("humaneval testing")
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
            print(str(compilation_output.stderr).lower()[:100])
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            print(str(output.stderr))
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "exception" in str(output.stderr).lower() or "error" in str(output.stderr).lower():
            print(str(output.stderr))
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            print("passed")
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        print(e)
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]

def test_java_ep(solution_generated, org_solution, main):
    print("evalplus testing")
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
            print(str(compilation_output.stderr).lower()[:100])
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            print(str(output.stderr))
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "exception" in str(output.stderr).lower() or "error" in str(output.stderr).lower():
            print(str(output.stderr))
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            print("passed")
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        print(e)
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        print(e)
        return 0, CODE_RUN_STATUS["COMPILATION"]


def test_cpp(prompt, code, main, new_entry_point, old_entry_point):
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
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main
    with open(f"../{testing_folder}/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir(f"../{testing_folder}/")

    try:
        if os.path.exists(f'../{testing_folder}/cpp_code'):
            subprocess.run(['rm', f'../{testing_folder}/cpp_code'], capture_output=False)
    except:
        None

    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=20, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            return 0, CODE_RUN_STATUS["COMPILATION"]

        # if os.path.exists("./cpp_code"):
        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)
        # else:
        #     return 0, CODE_RUN_STATUS["COMPILATION"]

        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "segmentation fault" in str(output.stderr).lower() or "error" in str(output.stderr).lower() or "terminate" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    # except subprocess.CalledProcessError as e:
    #     return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    # except Exception as e:
    #     return 0, CODE_RUN_STATUS["COMPILATION"]

def test_js(prompt, gc, main, new_entry_point, old_entry_point):
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
        line_cmnt = gc.find(f"//", gc.find("const"))
        if line_cmnt > 0:
            gc = gc[:line_cmnt]

    main = main.replace(old_entry_point, new_entry_point)
    full_code = gc + main

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

    # except subprocess.CalledProcessError as e:
    #     return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
def test_file(generated_path, lang):
    generated_data = load_prompts(generated_path)
    nominal_data =  get_nominal_prompts(lang)

    generated_data.sort(key=lambda x: x["task_id"])
    nominal_data.sort(key=lambda x: x["task_id"])

    result = {}
    for i in range(164):
        assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]

        if lang == "cpp":
            passed_status_he, run_status_he = test_cpp(generated_data[i]["prompt"], generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
            eval_main = get_evalplus_test_cases(lang, generated_data[i]["task_id"])
            passed_status_ep, run_status_ep = test_cpp(generated_data[i]["prompt"], generated_data[i]["gc"], eval_main, generated_data[i]["entry_point"])

        elif lang == "java":
            # if generated_data[i]["task_id"] not in ["Java/105","Java/162","Java/22","Java/34","Java/46"]:
            # if generated_data[i]["task_id"] not in ["Java/50", "Java/38", "Java/56"]["Java/20", "Java/32", "Java/63"]::
            # if generated_data[i]["task_id"] not in ["Java/20"]:
            #     continue
            test_he = java_imports + generated_data[i]["test"]
            test_ep = get_evalplus_main_class_for_java(generated_data[i]["task_id"])
            solution_gc = filter_java_solution(generated_data[i]["gc"], generated_data[i]["prompt"], nominal_data[i]["entry_point"], generated_data[i]["entry_point"])
            solution_org = get_evalplus_slution_for_java(generated_data[i]["task_id"])
            # print(generated_data[i]["gc"])
            # print(solution_gc)
            # print("-"*100)
            # print(solution_gc.replace("Solution", "SolutionGenerated"))
            # print("=" * 100)

            passed_status_he, run_status_he = test_java_he(solution_gc, test_he)
            passed_status_ep, run_status_ep = test_java_ep(solution_gc.replace("Solution", "SolutionGenerated"), solution_org, test_ep)

            print(generated_data[i]["task_id"], passed_status_he, passed_status_ep)
        elif lang == "js":
            passed_status, run_status = test_js(generated_data[i]["prompt"], generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        # generated_data[i]["passed"] = passed_status
        # generated_data[i]["run_status"] = run_status
    return generated_data

lang = "java"
testing_folder = "testing_dir5"
generated_path = "../datasets/incoder6b/generated_pass5_1/java/partial/f_s0.jsonl"
evalplus_dir = "/home/frabbi/Desktop/evalplus_all"

res = test_file(generated_path, lang)

# print(sum([r["passed"] for r in res]))