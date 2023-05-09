import json
import pdb
import pickle
from tqdm import tqdm as tq
import os
import subprocess
from collections import Counter
import pandas as pd

def view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"])
    prompts.sort(key=lambda x: x["task_id"])
    return prompts

def full_view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"]+json.loads(line)["canonical_solution"])
    prompts.sort(key=lambda x: x["task_id"])
    return prompts

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    prompts.sort(key=lambda x: x["task_id"])
    return prompts

def test_it(code, main, new_entry_point, i):
    if "<|endoftext|>" in code:
        code = code[:code.find("<|endoftext|>")]
    if "int main()" in code:
        code = code[:code.find("int main()")]
    old_entry_point = nominal_prompts[i]["entry_point"]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main
    with open("../tmp/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")

    try:
        # run g++ command to compile Java code
        compile_output = subprocess.check_output(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], stderr=subprocess.STDOUT)

        # run program to execute Main class
        run_output = subprocess.check_output(['./cpp_code'], stderr=subprocess.STDOUT, timeout=3)

        # print the output from the Java program
        return 1
        print(f"{i} successful")
        print(run_output.decode('utf-8'))
        return 1

    except subprocess.CalledProcessError as e:
        return 0
        # print the error message and output from the Java compiler or program
        print(f"{i}failed")
        # print("*"*50)
        # print(code)
        # print("*" * 50)
        print("An error occurred while running the program:")
        print(e.output.decode('utf-8'))
        print("Return code: ", e.returncode)
        return 0
        # import pdb; pdb.set_trace()
        # print()
    except subprocess.TimeoutExpired as e:
        return 0
        print(f"{i} timeout")

def get_test_result(filepath):
    prompts = load_prompts(filepath)
    result = {}
    for i in range(164):
        result[i] = test_it(prompts[i]["gc"], prompts[i]["test"], prompts[i]["entry_point"], i)
    return result

def get_report(directory, K):
    report = {}
    for i in range(K):
    # for filename in os.listdir(directory):
        filename = os.path.join(directory, f"f_s{i}.jsonl")
        result = get_test_result(filename)
        print(f"result ready for {filename}")
        report = {k: report.get(k, 0) + result.get(k, 0) for k in set(report) | set(result)}

    return report

# print(Counter(get_report("../datasets/generated/cpp/partial").values()))
# print(Counter(get_report("../datasets/generated/cpp/nominal").values()))

nominal_prompts = load_prompts("../datasets/nominal/HumanEval_cpp.jsonl")
nominal_prompts.sort(key=lambda x: x["task_id"])

datasets_path = "../datasets/codegen6bmulti/generated_pass5_1"
methods = ["nlaugmenter", "natgen", "format", "func_name"]
def get_result_dict(lang, K):
    result_dict = {}
    # for method in ['nominal', 'partial']:
    #     method_path = os.path.join(os.path.join(datasets_path, lang), method)
    #     print(method_path)
    #     report = get_report(method_path, K)
    #     result_dict[f"{lang}_{method}"] = Counter(report.values())
    #     print(f"{lang}_{method} done!!!")
    for method in methods:
        method_path = os.path.join(os.path.join(datasets_path, lang), method)
        for aug_method in os.listdir(method_path):
            aug_method_path = os.path.join(method_path,aug_method)
            print(aug_method_path)
            report = get_report(aug_method_path, K)
            result_dict [f"{lang}_{method}_{aug_method}"] = Counter(report.values())
            print(f"{lang}_{method}_{aug_method} done!!!")
    print(f"report ready for {lang} and {K}!!")
    return result_dict

for lang in ["cpp"]:
    for K in [5]:
        pd.DataFrame(get_result_dict(lang, K)).sort_index().to_csv(f"../datasets/result_rd5/{lang}_K_{K}.csv", index=True)

# lang = "cpp"
# result_dict = get_result_dict(lang)
#
# pd.DataFrame(result_dict).sort_index().to_csv(f"../datasets/result/{lang}.csv", index=True)
#
# with open(f"../datasets/result/{lang}.pickle", 'wb') as f:
#     pickle.dump(result_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open(f"../datasets/result/{lang}.json", "w") as f:
#     json.dump(result_dict, f)
# #
import pdb; pdb.set_trace()
#







# path = "../datasets/nominal/HumanEval_cpp.jsonl"
#
# prompts = load_prompts(path)
#
# for i in range(164):
#     test_it(prompts[i]["prompt"]+prompts[i]["canonical_solution"], prompts[i]["test"], i)

# pdb.set_trace()