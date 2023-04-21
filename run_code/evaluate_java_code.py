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


# for i in tq(range(len(prompts))):
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


def test_it(solution, main, new_entry_point, i):
    old_entry_point = nominal_prompts[i]["entry_point"]

    solution = solution[:solution.find("<|endoftext|>")]
    solution=eliminate_second_Sollution(solution)
    main = main.replace(old_entry_point, new_entry_point)
    # print((old_entry_point, new_entry_point))

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
        # run javac command to compile Java code
        compile_output = subprocess.check_output(['javac', 'Main.java', 'Solution.java'], stderr=subprocess.STDOUT)

        # run java command to execute Main class
        run_output = subprocess.check_output(['java', 'Main'], stderr=subprocess.STDOUT, timeout=3)

        # print the output from the Java program
        print(f"{i} successful")
        print(run_output.decode('utf-8'))
        return 1

    except subprocess.CalledProcessError as e:
        # print the error message and output from the Java compiler or program
        print(f"{i} failed")
        print("An error occurred while running the program:")
        # print("*"*50)
        # print(solution)
        # print("*" * 50)
        # print(main)
        # print("*" * 50)

        print(e.output.decode('utf-8'))
        print("Return code: ", e.returncode)
        # import pdb; pdb.set_trace()
        # print()
        return 0
    except subprocess.TimeoutExpired as e:
        print(f"{i} timeout")
        return 0

nominal_prompts = load_prompts("../datasets/nominal/HumanEval_java.jsonl")

# path = "../datasets/nominal/HumanEval_java.jsonl"
# operand_swap_path_prompts = load_prompts("../datasets/generated/java/natgen/OperandSwap/f_0.jsonl")
# operand_swap_path_prompts.sort(key=lambda x: x['task_id'])
# partial_prompts = load_prompts("../datasets/nominal/humanevaljava_partial.jsonl")
# partial_prompts.sort(key=lambda x: x['task_id'])
# default_prompts = load_prompts("../datasets/generated/java/nominal/f_0.jsonl")
# default_prompts.sort(key=lambda x: x['task_id'])


# snake_case_prompts = load_prompts("../datasets/generated/java/func_name/FuncRenameSnakeCase/f_0.jsonl")
# pert_prompts = load_prompts("../datasets/generated/java/func_name/FuncRenameChangeChar/f_0.jsonl")
#
# def_res = {}
# for i in range(164):
#     def_res[i] = test_it(default_prompts[i]["gc"], default_prompts[i]["test"], default_prompts[i]["entry_point"], i)
# print(def_res)
# per_res = {}
# for i in range(164):
#     per_res[i] = test_it(operand_swap_path_prompts[i]["gc"], operand_swap_path_prompts[i]["test"], operand_swap_path_prompts[i]["entry_point"], i)
# print(per_res)
# df = pd.DataFrame({"default":def_res, "op_swap":per_res})
# df.to_csv("../datasets/result/def_v_swap.csv")

# pdb.set_trace()

#
# pdb.set_trace()


def get_test_result(filepath):
    prompts = load_prompts(filepath)
    result = {}
    for i in range(164):
        # print(i)
        # prompt = prompts[i]

        sample_java_main = "import java.util.ArrayList;\n" \
           "import java.util.Arrays;\n" \
           "import java.util.List;\n" \
           "import java.util.Objects;\n" \
           "import java.util.Map;\n" \
           "import java.util.Random;\n" \
           "import java.util.HashMap;\n" \
           "import java.util.Optional;\n" \
           "import java.security.NoSuchAlgorithmException;\n" \
           + prompts[i]["test"]
        #updating the main.java because it calls the method from solution.java. the method may change because of function renaming
        sample_java_main = sample_java_main.replace(nominal_prompts[i]["entry_point"], prompts[i]["entry_point"])

        sample_java_solution = prompts[i]["gc"]

        if "<|endoftext|>" in sample_java_solution:
            sample_java_solution = sample_java_solution[:sample_java_solution.find("<|endoftext|>")]
        sample_java_solution = eliminate_second_Sollution(sample_java_solution)

        with open("../tmp/Main.java", "w") as f:
            f.write(sample_java_main)
        with open("../tmp/Solution.java", "w") as f:
            f.write(sample_java_solution)
        os.chdir("../tmp/")

        try:
            # run javac command to compile Java code
            compile_output = subprocess.check_output(['javac', 'Main.java', 'Solution.java'], stderr=subprocess.STDOUT)

            # run java command to execute Main class
            run_output = subprocess.check_output(['java', 'Main'], stderr=subprocess.STDOUT, timeout=3)

            result[i]=1
            # print the output from the Java program
            # print(f"{i} successful")
            # print(run_output.decode('utf-8'))


        except subprocess.CalledProcessError as e:
            result[i]=0
            # print the error message and output from the Java compiler or program
            # print(f"{i} failed")
            # print("An error occurred while running the program:")
            # print(e.output.decode('utf-8'))
            # print("Return code: ", e.returncode)
            # import pdb; pdb.set_trace()
            # print()
        except subprocess.TimeoutExpired as e:
            result[i] = 0

        # try:
        #     subprocess.check_output(['rm', 'Main.java', 'Solution.java', 'Main.class', 'Solution.class'])
        # except:
        #     print("can not delete files")

        # print(f"finished!! {i}")
    return result

# import pdb; pdb.set_trace()



def get_report(directory, K):
    report = {}
    for i in range(K):
    # for filename in os.listdir(directory):
        filename = os.path.join(directory, f"f_{i}.jsonl")
        result = get_test_result(filename)
        print(f"result ready for {filename}")
        report = {k: report.get(k, 0) + result.get(k, 0) for k in set(report) | set(result)}

    return report

# print("partial")
# print(Counter(get_report("../datasets/generated/java/partial").values()))
# print("nominal")
# print(Counter(get_report("../datasets/generated/java/nominal").values()))

##checking get_report with only one directory
# print("butter", Counter(get_report("../datasets/generated/java/nlaugmenter/ButterFingersPerturbation").values()))
# print("char",Counter(get_report("../datasets/generated/java/nlaugmenter/ChangeCharCase").values()))
# print("back", Counter(get_report("../datasets/generated/java/nlaugmenter/BackTranslation").values()))
# pdb.set_trace()


# dataset_names = ['py', 'java', 'cpp', 'js', 'go']
datasets_path = "../datasets/generated"
langs = ['java']
methods = ["nlaugmenter", "natgen", "format", "func_name"]
def get_result_dict(lang, K):
    result_dict = {}
    for method in ['nominal', 'partial']:
        method_path = os.path.join(os.path.join(datasets_path, lang), method)
        print(method_path)
        report = get_report(method_path, K)
        result_dict[f"{lang}_{method}"] = Counter(report.values())
        print(f"{lang}_{method} done!!!")
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

# K = 1
# lang = "java"
# result_dict = get_result_dict(lang, K)

# with open(f"../datasets/result/{lang}.pickle", 'rb') as f:
#     result_dict = pickle.load(f)
#
for lang in ["java"]:
    for K in [1, 5, 10]:
        pd.DataFrame(get_result_dict(lang, K)).sort_index().to_csv(f"../datasets/result/{lang}_K_{K}.csv", index=True)
#
# with open(f"../datasets/result/{lang}.pickle", 'wb') as f:
#     pickle.dump(result_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open(f"../datasets/result/{lang}.json", "w") as f:
#     json.dump(result_dict, f)
#
import pdb; pdb.set_trace()