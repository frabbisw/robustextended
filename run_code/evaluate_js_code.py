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


def test_it(code, main, new_entry_point, i):
    code = code[:code.find("<|endoftext|>")]
    # method_mark = code.find("const")
    # second_method_mark = code.find("const", method_mark)
    # if second_method_mark >= 0:
    #     code = code[:second_method_mark]
    old_entry_point = nominal_prompts[i]["entry_point"]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main

    print("#" * 20)
    print(partial_prompts[i]["prompt"])
    print("1" * 20)
    print(perturbed_prompts[i]["prompt"])
    print("2" * 20)
    print(code)
    print("3" * 20)
    print(main)
    print("#" * 20)

    with open("../tmp/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")
    try:
        # run node command to execute full code
        run_output = subprocess.check_output(['node', 'Sample.js'], stderr=subprocess.STDOUT, timeout=3)

        # print("#" * 20)
        # print(partial_prompts[i]["prompt"])
        # print("*" * 20)
        # print(perturbed_prompts[i]["prompt"])
        # print("*" * 20)
        # print(code)
        # print("*" * 20)
        # print(main)
        # print("#" * 20)

        print(f"{i} successful")
        # print(run_output.decode('utf-8'))
        return 1

    except subprocess.CalledProcessError as e:
        # print(f"{i} failed")
        # print("An error occurred while running the program:")
        # print("*"*50)
        # print(code)
        # print("*" * 50)
        # print(main)
        # print("*" * 50)
        #
        # print(e.output.decode('utf-8'))
        # print("Return code: ", e.returncode)
        # import pdb; pdb.set_trace()
        # print()
        return 0
    except subprocess.TimeoutExpired as e:
        # print(f"{i} timeout")
        return 0

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
        filename = os.path.join(directory, f"f_{i}.jsonl")
        result = get_test_result(filename)
        print(f"result ready for {filename}")
        report = {k: report.get(k, 0) + result.get(k, 0) for k in set(report) | set(result)}

    return report

nominal_prompts = load_prompts("../datasets/nominal/HumanEval_js.jsonl")
nominal_prompts.sort(key=lambda x: x["task_id"])

datasets_path = "../datasets/generated"
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

# for lang in ["js"]:
#     for K in [10]:
#         pd.DataFrame(get_result_dict(lang, K)).sort_index().to_csv(f"../datasets/result/{lang}_K_{K}.csv", index=True)

# perturbed_prompts = load_prompts("../datasets/generated/js/natgen/ForWhileTransformer/f_0.jsonl")
# perturbed_prompts = load_prompts("../datasets/generated/js/natgen/DeadCodeInserter/f_0.jsonl")
perturbed_prompts = load_prompts("../datasets/generated/js/natgen/OperandSwap/f_0.jsonl")
# perturbed_prompts = load_prompts("../datasets/generated/js/natgen/VarRenamerRN/f_0.jsonl")
# perturbed_prompts = load_prompts("../datasets/generated/js/natgen/VarRenamerCB/f_0.jsonl")
# perturbed_prompts = load_prompts("../datasets/generated/js/natgen/VarRenamerNaive/f_0.jsonl")

perturbed_prompts.sort(key=lambda x: x["task_id"])
partial_prompts = load_prompts("../datasets/nominal/humanevaljs_partial.jsonl")
partial_prompts.sort(key=lambda x: x["task_id"])

# import pdb; pdb.set_trace();

for i in range(164):
    print(i, test_it(perturbed_prompts[i]["gc"], perturbed_prompts[i]["test"], perturbed_prompts[i]["entry_point"], i) * "passed")

# report = get_report("../datasets/generated/js/natgen/VarRenamerRN", 4)
# dict_count = Counter(report.values())
#
# print(dict_count)

# import pdb; pdb.set_trace()