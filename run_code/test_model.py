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

CODE_RUN_STATUS = {"PASSED": 0, "ASSERTION": 1, "COMPILATION": 2, "TIMEOUT": 3, "RUNTIME": 4}


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
            prompts.append(json.loads(line)["prompt"] + json.loads(line)["canonical_solution"])
    return prompts


def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts


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
    return sample_java_solution[:sample_java_solution.rfind("}") + 1]


def test_java(solution, main, new_entry_point, old_entry_point):
    if "<|endoftext|>" in solution:
        solution = solution[:solution.find("<|endoftext|>")]
    solution = solution[:solution.find("<|endoftext|>")]
    solution = eliminate_second_Sollution(solution)

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
    with open("../testing_dir5/Main.java", "w") as f:
        f.write(main)
    with open("../testing_dir5/Solution.java", "w") as f:
        f.write(solution)
    os.chdir("../testing_dir5/")
    try:
        compilation_output = subprocess.run(['javac', 'Main.java', 'Solution.java'], timeout=4, capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            print("="*50)
            print(solution)
            print("COMPILATIONERROR")
            print("="*50)
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['java', 'Main'], timeout=4, capture_output=True)
        try:
            subprocess.run(['rm', '../testing_dir/Solution.class', '../testing_dir/Main.class'], capture_output=False)
            # subprocess.run(['rm', '../testing_dir/*.class', '../testing_dir/*.java'], capture_output=False)

        except:
            None
        if "assertion" in str(output.stderr).lower():
            print("="*50)
            print(solution)
            print("ASSERTIONERROR")
            print("="*50)
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
        print("=" * 50)
        print(solution)
        print("COMPILATIONERROR")
        print("=" * 50)
        return 0, CODE_RUN_STATUS["COMPILATION"]


def test_cpp(code, main, new_entry_point, old_entry_point):
    code = code.replace("usingnamespace", "using namespace")
    code = code.replace("using std;", "using namespace std;")
    if "<|endoftext|>" in code:
        code = code[:code.find("<|endoftext|>")]
    cmnt_index = code.find("/*")
    cmnt_index = code.find("/*", cmnt_index + 5)
    if cmnt_index > 0:
        code = code[:cmnt_index]
    if "int main()" in code:
        code = code[:code.find("int main()")]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main

    with open("../testing_dir5/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../testing_dir5/")

    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=4,
                                            capture_output=True)
        if "error" in str(compilation_output.stderr).lower():
            print("COMPILATIONWITHERROR")
            print(compilation_output.stderr)
            print("=" * 50)
            print(code)
            print(" |code - main| " * 10)
            print(main)
            print(" |main - error| " * 10)
            print(str(compilation_output.stderr))
            print("=" * 50)
            return 0, CODE_RUN_STATUS["COMPILATION"]

        output = subprocess.run(['./cpp_code'], timeout=4, capture_output=True)
        try:
            subprocess.run(['rm', '../testing_dir/cpp_code'], timeout=4, capture_output=True)
        except:
            print(f"cant delete ../testing_dir/cpp_code")

        if "assertion" in str(output.stderr).lower():
            print("ASSERTIONERROR")
            print("=" * 50)
            print(code)
            print(" |code - main| " * 10)
            print(main)
            print(" |main - error| " * 10)
            print(str(output.stderr))
            print("=" * 50)
            # print(output.stderr)
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


def test_js(gc, main, new_entry_point, old_entry_point):
    gc = gc[:gc.find("<|endoftext|>")]
    cmnt_index = gc.find("/*")
    cmnt_index = gc.find("/*", cmnt_index + 5)
    if cmnt_index > 0:
        gc = gc[:cmnt_index]
    gc = gc.replace(" \\\n", "\n")
    main = main.replace(old_entry_point, new_entry_point)
    full_code = gc + main

    # print(full_code)
    # print("*"*50)

    with open("../testing_dir5/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir("../testing_dir5/")
    try:
        output = subprocess.run(['node', 'Sample.js'], timeout=4, capture_output=True)
        # print(full_code)
        if "assertion" in str(output.stderr).lower():
            # print(output.stderr)
            return 0, CODE_RUN_STATUS["ASSERTION"]
        elif "error" in str(output.stderr).lower():
            print(output.stderr)
            return 0, CODE_RUN_STATUS["COMPILATION"]
        else:
            return 1, CODE_RUN_STATUS["PASSED"]

    except subprocess.CalledProcessError as e:
        return 0, CODE_RUN_STATUS["COMPILATION"]
    except subprocess.TimeoutExpired as e:
        return 0, CODE_RUN_STATUS["TIMEOUT"]


def test_file(generated_path, lang):
    generated_data = load_prompts(generated_path)
    nominal_data = get_nominal_prompts(lang)

    generated_data.sort(key=lambda x: x["task_id"])
    nominal_data.sort(key=lambda x: x["task_id"])

    result = {}
    for i in range(164):
        if lang == "cpp":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_cpp(generated_data[i]["gc"], generated_data[i]["test"],
                                                 generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        elif lang == "java":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_java(generated_data[i]["gc"], generated_data[i]["test"],
                                                  generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        elif lang == "js":
            assert generated_data[i]["task_id"] == nominal_data[i]["task_id"]
            passed_status, run_status = test_js(generated_data[i]["gc"], generated_data[i]["test"],
                                                generated_data[i]["entry_point"], nominal_data[i]["entry_point"])
        generated_data[i]["passed"] = passed_status
        generated_data[i]["run_status"] = run_status
    return generated_data


def get_nominal_prompts(lang):
    return load_prompts(f"../datasets/nominal/HumanEval_{lang}.jsonl")


# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/cpp/natgen/VarRenamerNaive/f_s0.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/cpp/natgen/OperandSwap/f_s0.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/java/nominal/f_s0.jsonl"
# generated_path = "../datasets/codegen2bmulti/generated_pass5_1/js/format/new_line_afterdoc/f_s0.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/cpp/partial/f_s0.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/cpp/partial/f_s0.jsonl"
# generated_path = "../testing_dir/gg.jsonl"
# generated_path = "../datasets/codegen2bmulti/generated_pass5_1/js/natgen/OperandSwap/f_s0.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/js/partial/f_s0.jsonl"
# generated_path = "../testing_dir/cg6b_nlac_lab.jsonl"
# generated_path = "../testing_dir/cg6b_nlac_lab.jsonl"
# generated_path = "../datasets/codegen6bmulti/generated_pass5_1/js/partial/f_s0.jsonl"

generated_path = "../datasets/incoder6b/generated_pass5_1/java/nominal/f_s0.jsonl"
generated_data = test_file(generated_path, "java")
print(sum(d["passed"] for d in generated_data))
print("%%" * 100)

# prompts = load_prompts(generated_path)
# # print(prompts[0]["gc"] +"\n"+ prompts[0]["test"])
#
# res = test_js(prompts[0]["gc"], prompts[0]["test"], prompts[0]["entry_point"], prompts[0]["entry_point"])
# print(res)

# import pdb; pdb.set_trace()


# prompts = load_prompts(generated_path)

# import pdb;pdb.set_trace()