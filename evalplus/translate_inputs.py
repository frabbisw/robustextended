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
evalplusdirectory = "evalplusdata"
def save_java(code, entry_point, task_inputs, orgmain, task_id):
    main = "public class Main {\n" + create_map_string +"\tpublic static void main(String[] args) throws NoSuchAlgorithmException {\n\t\tSolution s = new Solution();\n"
    for i in task_inputs:
        main += f"\t\ts.{entry_point}({i});\n"
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
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplusdirectory}/java/{folder_name}"):
        os.mkdir(f"/home/frabbi/Desktop/{evalplusdirectory}/java/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/java/{folder_name}/Main.java", "w") as f:
        f.write(main)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/java/{folder_name}/OrgMain.java", "w") as f:
        f.write(orgmain)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/java/{folder_name}/Solution.java", "w") as f:
        f.write(code)

with open("cpp_helper.txt", "r") as f:
    cpp_tostring = f.read()
def save_cpp(code, entry_point, task_inputs, orgmain, task_id):
    main = "#undef NDEBUG\n#include<assert.h>\n#include <iostream>\nusing namespace std;\nint main(){\n"
    for i in task_inputs:
        main += f"\t{entry_point}({i});\n"
        # main += f"\tcout << \"#\";\n"
    main += "}"
    main = cpp_tostring +"\n"+ main + "\n"
    full_code = code + "\n" + main

    folder_name = task_id.replace("/", "")
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}"):
        os.mkdir(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}/solution.cpp", "w") as f:
        f.write(code)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}/orgmain.cpp", "w") as f:
        f.write(orgmain)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}/main.cpp", "w") as f:
        f.write(main)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/cpp/{folder_name}/fullcode.cpp", "w") as f:
        f.write(full_code)
    return 0

with open("js_helper.txt", "r") as f:
    js_tostring = f.read()
def save_js(code, entry_point, task_inputs, orgmain, task_id):
    main = js_tostring + "\n"

    for i in task_inputs:
        # full_code += f"console.log({entry_point}({i}));\n"
        # full_code += f"console.log(\"#\");\n"

        main += f"{entry_point}({i});\n"
        # main += f"process.stdout.write(\"#\");\n"

    full_code = code + "\n" + main + "\n"

    folder_name = task_id.replace("/", "")
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}"):
        os.mkdir(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}/solution.js", "w") as f:
        f.write(code)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}/fullcode.js", "w") as f:
        f.write(full_code)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}/main.js", "w") as f:
        f.write(main)
    with open(f"/home/frabbi/Desktop/{evalplusdirectory}/js/{folder_name}/orgmain.js", "w") as f:
        f.write(orgmain)

def save_inputs(prompts, inputs, lang):
    for prompt in prompts:
        task_id = prompt["task_id"]
        if task_id.split("/")[-1] in ['21', '22', '32', '39', '44', '49', '55', '63', '64', '76', '91', '95', '96', '97', '111', '122', '123', '124', '125', '126', '127', '132', '139', '140', '150']:
            task_inputs = inputs[task_id]
            solution = prompt["prompt"] + prompt["canonical_solution"]
            if lang == "java":
                save_java(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)
            elif lang == "cpp":
                save_cpp(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)
            elif lang == "js":
                save_js(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)

save_inputs(java_prompts, java_inputs, "java")
print("="*50)
# print("="*50)
save_inputs(js_prompts, js_inputs, "js")
print("="*50)
save_inputs(cpp_prompts, cpp_inputs, "cpp")

# def generate_test_(lang):
#     inputs = {"java":java_inputs, "cpp":cpp_inputs, "js":js_inputs}[lang]

