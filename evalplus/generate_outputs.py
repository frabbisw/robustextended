import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import subprocess
import re
import time

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

evalplus_type = "full"
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
    main = "public class Main {\n" + create_map_string +"\tpublic static void main(String[] args) throws NoSuchAlgorithmException {\n\t\tSolution s = new Solution();\n"
    for i in task_inputs:
        main += f"\t\tSystem.out.print(s.{entry_point}({i}));\n"
        # main += f"\t\tSystem.out.print(\"#\");\n"
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

    folder_name = task_id.replace("/", "")
    os.mkdir(f"/home/frabbi/Desktop/evalplusdata/java/{folder_name}")
    with open(f"/home/frabbi/Desktop/evalplusdata/java/{folder_name}/Main.java", "w") as f:
        f.write(main)
    with open(f"/home/frabbi/Desktop/evalplusdata/java/{folder_name}/OrgMain.java", "w") as f:
        f.write(orgmain)
    with open(f"/home/frabbi/Desktop/evalplusdata/java/{folder_name}/Solution.java", "w") as f:
        f.write(code)



    return 0

    with open("../testing_dir/Main.java", "w") as f:
        f.write(main)
    with open("../testing_dir/Solution.java", "w") as f:
        f.write(code)
    os.chdir("../testing_dir/")
    try:
        # print(task_id)
        compilation_output = subprocess.run(['javac', 'Main.java', 'Solution.java'], timeout=5, capture_output=True)
        # timeStarted = time.time()
        output = subprocess.run(['java', 'Main'], timeout=8, capture_output=True)
        # timeDelta = time.time() - timeStarted
        # print("Finished process in " + str(timeDelta) + " seconds.")
        # print("*"*50)
        # print(output.stdout.decode())

        if len(output.stdout.decode()) < 10:
            print(task_id)
            print(f"#{output.stdout.decode()[:100]}#")

        if "error" in compilation_output.stderr.decode():
            print(task_id)
            # print(compilation_output.stderr.decode()[:300])
            # print(task_inputs)
            # print(code)
            # print(main)
            # print(orgmain)
            print("*"*50)
            # exit()
        if "error" in output.stderr.decode().lower():
            print(task_id)
            print("+"*50)
        # print("*" * 50)
    except Exception as e:
        print(task_id)
        print(e)
    # print(code)
    # print(main)

with open("cpp_helper.txt", "r") as f:
    cpp_tostring = f.read()
def run_cpp(code, entry_point, task_inputs, orgmain, task_id):
    main = "#undef NDEBUG\n#include<assert.h>\n#include <iostream>\nusing namespace std;\nint main(){\n"
    for i in task_inputs:
        main += f"\tcout << toString({entry_point}({i}));\n"
        # main += f"\tcout << \"#\";\n"
    main += "}"
    main = cpp_tostring +"\n"+ main + "\n"
    full_code = code + "\n" + main

    folder_name = task_id.replace("/", "")
    os.mkdir(f"/home/frabbi/Desktop/evalplusdata/cpp/{folder_name}")
    with open(f"/home/frabbi/Desktop/evalplusdata/cpp/{folder_name}/code.cpp", "w") as f:
        f.write(code)
    with open(f"/home/frabbi/Desktop/evalplusdata/cpp/{folder_name}/orgmain.cpp", "w") as f:
        f.write(orgmain)
    with open(f"/home/frabbi/Desktop/evalplusdata/cpp/{folder_name}/main.cpp", "w") as f:
        f.write(main)
    return 0

    with open("../testing_dir/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../testing_dir/")

    try:
        compilation_output = subprocess.run(['g++', '-o', 'cpp_code', 'cpp_code.cpp', '-lcrypto', '-lssl'], timeout=5, capture_output=True)
        # timeStarted = time.time()
        output = subprocess.run(['./cpp_code'], timeout=8, capture_output=True)
        # timeDelta = time.time() - timeStarted
        # print("Finished process in " + str(timeDelta) + " seconds.")
        if len(output.stdout.decode()) < 10:
            print(task_id)
            print(f"#{output.stdout.decode()[:100]}#")

        if "error" in compilation_output.stderr.decode():
            print(task_id)
            # print(compilation_output.stderr.decode()[:300])
            # print(task_inputs)
            # print(code)
            # print(main)
            # print(orgmain)
            print("*"*50)
            # exit()
        if "error" in output.stderr.decode().lower():
            print(task_id)
            print("+"*50)
        # print(output.stdout.decode())
        # print(compilation_output.stderr.decode(), output.stderr.decode())

    except Exception as e:
        print(task_id)
        print(e)

with open("js_helper.txt", "r") as f:
    js_tostring = f.read()
def run_js(code, entry_point, task_inputs, orgmain, task_id):
    main = js_tostring + "\n"

    for i in task_inputs:
        # full_code += f"console.log({entry_point}({i}));\n"
        # full_code += f"console.log(\"#\");\n"

        main += f"process.stdout.write(toString({entry_point}({i})));\n"
        # main += f"process.stdout.write(\"#\");\n"

    full_code = main + "\n" + code + "\n"

    folder_name = task_id.replace("/", "")
    os.mkdir(f"/home/frabbi/Desktop/evalplusdata/js/{folder_name}")
    with open(f"/home/frabbi/Desktop/evalplusdata/js/{folder_name}/code.js", "w") as f:
        f.write(code)
    with open(f"/home/frabbi/Desktop/evalplusdata/js/{folder_name}/orgmain.js", "w") as f:
        f.write(orgmain)
    with open(f"/home/frabbi/Desktop/evalplusdata/js/{folder_name}/main.js", "w") as f:
        f.write(main)
    return 0

    with open("../testing_dir/js_code.js", "w") as f:
        f.write(full_code)
    os.chdir("../testing_dir/")

    try:
        # timeStarted = time.time()
        output = subprocess.run(['node', 'js_code.js'], timeout=8, capture_output=True)
        print(task_id)
        # print(full_code)
        # print(f"#{output.stdout.decode()[:100]}#")
        # timeDelta = time.time() - timeStarted  # Get execution time.
        # print("Finished process in " + str(timeDelta) + " seconds.")
        # print("$"*50)
        # exit()
        if "error" in output.stderr.decode():
            print(task_id)
        #     print(output.stderr.decode()[:300])
        #     # print(task_inputs)
        #     print(code)
        #     print(full_code)
        #     print(orgmain)
            print("*" * 50)
            # exit()
    except Exception as e:
        print(task_id)
        # print("@"*50)
        print(e)
    # exit()


def generate_output(prompts, inputs, lang):
    for prompt in prompts:
        task_id = prompt["task_id"]
        if task_id != "CPP/123":
            continue
        task_inputs = inputs[task_id]
        full_code = prompt["prompt"] + prompt["canonical_solution"]
        if lang == "java":
            run_java(full_code, prompt["entry_point"], task_inputs, prompt["test"], task_id)
        elif lang == "cpp":
            run_cpp(full_code, prompt["entry_point"], task_inputs, prompt["test"], task_id)
        elif lang == "js":
            run_js(full_code, prompt["entry_point"], task_inputs, prompt["test"], task_id)

# prompt = java_prompts[0]
# inputs = java_inputs[prompt["task_id"]]
# lang = "java"

generate_output(java_prompts, java_inputs, "java")
# print("="*50)
generate_output(cpp_prompts, cpp_inputs, "cpp")
# print("="*50)
generate_output(js_prompts, js_inputs, "js")

# def generate_test_(lang):
#     inputs = {"java":java_inputs, "cpp":cpp_inputs, "js":js_inputs}[lang]

