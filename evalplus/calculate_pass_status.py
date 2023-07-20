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
    backup = solution
    start_index = solution.find("<|endoftext|>")
    if start_index < 0:
        start_index = 0
    elif start_index < 5:
        start_index = start_index + len("<|endoftext|>")
    else:
        start_index = 0
    end_index = solution.rfind("<|endoftext|>")
    if end_index < 5:
        end_index = len(solution)

    solution = solution[start_index:end_index]

    if f"</code>" in solution:
        solution = solution[:solution.find("</code>")]
    if f"<code>" in solution:
        solution = solution[solution.find("<code>"):]

    solution = eliminate_second_Sollution(solution)
    solution = solution.replace(new_entry_point, old_entry_point)
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
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=5, capture_output=True)
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
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)

        if "assertion" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "segmentation fault" in str(output.stderr).lower() or "error" in str(output.stderr).lower() or "terminate" in str(output.stderr).lower():
            return 0, CODE_RUN_STATUS["RUNTIME"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]
    except Exception as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]

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
def test_file(generated_path, lang):
    generated_data = load_prompts(generated_path)
    nominal_data =  get_nominal_prompts(lang)

    generated_data.sort(key=lambda x: x["task_id"])
    nominal_data.sort(key=lambda x: x["task_id"])

    result = {}
    for i in range(164):
        if lang == "js":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            main_method = get_evalplus_test_cases(lang, generated_data[i]["task_id"])
            passed_status, run_status = test_js(generated_data[i]["gc"], main_method, generated_data[i]["entry_point"])
        elif lang == "cpp":
            if generated_data[i]["task_id"] == "CPP/32":
                generated_data[i]["entry_point"] = "find_zero"
            # if generated_data[i]["task_id"] in ["CPP/32", "CPP/87", "CPP/137"]:
            #     continue
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            main_method = get_evalplus_test_cases(lang, generated_data[i]["task_id"])
            passed_status, run_status = test_cpp(generated_data[i]["gc"], main_method, generated_data[i]["entry_point"])
        elif lang == "java":
            # if generated_data[i]["task_id"] in ["Java/32", "Java/87", "Java/55", "Java/63"]:
            #     continue
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            main_class = get_evalplus_main_class_for_java(generated_data[i]["task_id"])
            solution_class = get_evalplus_slution_for_java(generated_data[i]["task_id"])
            passed_status, run_status = test_java(generated_data[i]["gc"], solution_class, main_class, generated_data[i]["entry_point"], nominal_data[i]["entry_point"])

        #     passed_status, run_status = test_cpp(generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        # elif lang == "java":
        #     assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
        #     passed_status, run_status = test_java(generated_data[i]["gc"], generated_data[i]["test"], generated_data[i]["entry_point"], nominal_data[i]["entry_point"])

        generated_data[i]["passed_evalplus"] = passed_status
        generated_data[i]["run_status_evalplus"] = run_status
    return generated_data
def test_aug_method(directory, lang):
    print(directory)
    file_paths = [f for f in listdir(directory) if isfile(join(directory, f))]
    for file_name in file_paths:
        file_path = join(directory, file_name)
        # print(file_path)
        generated_data = test_file(file_path, lang)
        save_prompts(file_path, generated_data)

def get_nominal_prompts(lang):
    return load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")

# methods = []
# nominals = ["nominal"]
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


# print(test_js(generated_data[i]["gc"], main_method, generated_data[i]["entry_point"]))

# print(get_evalplus_test_cases("js", "JavaScript/134"))