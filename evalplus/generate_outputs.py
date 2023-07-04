import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import subprocess
import re

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

evalplus_type = "mini"
with open(f"java_inputs_{evalplus_type}", "rb") as f:
    java_inputs = pickle.load(f)
with open(f"cpp_inputs_{evalplus_type}", "rb") as f:
    cpp_inputs = pickle.load(f)
with open(f"js_inputs_{evalplus_type}", "rb") as f:
    js_inputs = pickle.load(f)


java_prompts = load_prompts("../datasets/nominal/humanevaljava_nominal_f_s0.jsonl")
cpp_prompts = load_prompts("../datasets/nominal/humanevalcpp_nominal_f_s0.jsonl")
js_prompts = load_prompts("../datasets/nominal/humanevaljs_nominal_f_s0.jsonl")

with open("java_create_map.txt", "r") as f:
    create_map_string = f.read()

def run_java(code, entry_point, task_inputs, orgmain, task_id):
    main = "public class Main {\n" + create_map_string +"\tpublic static void main(String[] args) {\n\t\tSolution s = new Solution();\n"
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
        # print(output.stdout.decode())
        if "error" in compilation_output.stderr.decode():
            print(task_id)
            print(compilation_output.stderr.decode())
            print(repr(task_inputs))
            print(code)
            print(main)
            print(repr(orgmain))
            print("*"*50)
            exit()

        # print("*" * 50)
    except Exception as e:
        print(e)
    # print(code)
    # print(main)

def run_cpp(code, entry_point, task_inputs):
    main = "#undef NDEBUG\n#include<assert.h>\n#include <iostream>\nusing namespace std;\nint main(){\n"
    for i in task_inputs:
        main += f"\tcout << {entry_point}({i});\n"
        main += f"\tcout << \"#\";\n"
    main += "}"
    full_code = code +"\n"+ main
    with open("../testing_dir/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../testing_dir/")
    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=10, capture_output=True)

        # exit()
        output = subprocess.run(['./cpp_code'], timeout=4, capture_output=True)
        print(output.stdout.decode())
        print(compilation_output.stderr.decode(), output.stderr.decode())

    except Exception as e:
        print(e)

def generate_output(prompts, inputs, lang):
    for prompt in prompts:
        task_id = prompt["task_id"]
        task_inputs = inputs[task_id]
        full_code = prompt["prompt"] + prompt["canonical_solution"]
        if lang == "java":
            run_java(full_code, prompt["entry_point"], task_inputs, prompt["test"], task_id)
        elif lang == "cpp":
            run_cpp(full_code, prompt["entry_point"], task_inputs)


# prompt = java_prompts[0]
# inputs = java_inputs[prompt["task_id"]]
# lang = "java"

generate_output(java_prompts, java_inputs, "java")
# generate_output(cpp_prompts, cpp_inputs, "cpp")


# def generate_test_(lang):
#     inputs = {"java":java_inputs, "cpp":cpp_inputs, "js":js_inputs}[lang]

