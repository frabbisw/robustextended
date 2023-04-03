import json
from tqdm import tqdm as tq
import os
import subprocess
from collections import Counter

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

# result_path = "../datasets/generated/HumanEval_java_350m.jsonl"

# prompts = load_prompts(result_path)

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

def get_test_result(filepath):
    prompts = load_prompts(filepath)
    result = {}
    for i in range(164):
        # print(i)
        # prompt = prompts[i]

        sample_java_main = "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.List;\n" + prompts[i]["test"]
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



def get_report(directory):
    report = {}
    for filename in os.listdir(directory):
        result = get_test_result(os.path.join(directory, filename))
        print(f"result ready for {filename}")
        report = {k: report.get(k, 0) + result.get(k, 0) for k in set(report) | set(result)}

    return report
# report = get_report("../datasets/generated/java/nominal")
# print(Counter(report.values()))
# report = get_report("../datasets/generated/java/deadcode")
# print(Counter(report.values()))
# report = get_report("../datasets/generated/java/docstring/humanevaljava_ButterFingersPerturbation")
# print(Counter(report.values()))
# report = get_report("../datasets/generated/java/docstring/humanevaljava_BackTranslation")
# print(Counter(report.values()))
# report = get_report("../datasets/generated/java/docstring/humanevaljava_SynonymInsertion")
# print(Counter(report.values()))

# report = get_report("../datasets/generated/java/docstring/humanevaljava_EnglishInflectionalVariation")
# print(Counter(report.values()))
#
# report = get_report("../datasets/generated/java/docstring/humanevaljava_SynonymSubstitution")
# print(Counter(report.values()))

report = get_report("../datasets/generated/java/func_name/humanevaljava_FuncRenameInflectionalVariation")
print(Counter(report.values()))

# import pdb; pdb.set_trace()