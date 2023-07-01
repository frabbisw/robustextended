import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import subprocess

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

with open("java_inputs", "rb") as f:
    java_inputs = pickle.load(f)
with open("cpp_inputs", "rb") as f:
    cpp_inputs = pickle.load(f)
with open("js_inputs", "rb") as f:
    js_inputs = pickle.load(f)


java_prompts = load_prompts("../datasets/nominal/humanevaljava_nominal_f_s0.jsonl")
cpp_prompts = load_prompts("../datasets/nominal/humanevalcpp_nominal_f_s0.jsonl")
js_prompts = load_prompts("../datasets/nominal/humanevaljs_nominal_f_s0.jsonl")


def run_java(code, entry_point, task_inputs):
    main = "public class Main {\n\tpublic static void main(String[] args) {\n\t\tSolution s = new Solution();\n"
    for i in task_inputs:
        main += f"\t\tSystem.out.print(s.{entry_point}({i}));\n"
        main += f"\t\tSystem.out.print(\"#\");\n"
    main += "\t}\n}\n"
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
    with open("../testing_dir/Main.java", "w") as f:
        f.write(main)
    with open("../testing_dir/Solution.java", "w") as f:
        f.write(code)
    os.chdir("../testing_dir/")
    try:
        compilation_output = subprocess.run(['javac', 'Main.java', 'Solution.java'], timeout=4, capture_output=True)
        output = subprocess.run(['java', 'Main'], timeout=4, capture_output=True)
        # print("*"*50)
        print(output.stdout.decode())
        # print("*" * 50)
    except Exception as e:
        print(e)
    # print(code)
    # print(main)
def generate_output(prompts, inputs, lang):
    for prompt in prompts:
        task_id = prompt["task_id"]
        task_inputs = inputs[task_id]
        full_code = prompt["prompt"] + prompt["canonical_solution"]
        if lang == "java":
            run_java(full_code, prompt["entry_point"], task_inputs)


# prompt = java_prompts[0]
# inputs = java_inputs[prompt["task_id"]]
# lang = "java"

generate_output(java_prompts, java_inputs, "java")


# def generate_test_(lang):
#     inputs = {"java":java_inputs, "cpp":cpp_inputs, "js":js_inputs}[lang]

