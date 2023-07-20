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

js_obj_special_ids = ['JavaScript/1', 'JavaScript/100', 'JavaScript/101', 'JavaScript/104', 'JavaScript/105', 'JavaScript/106', 'JavaScript/111', 'JavaScript/113', 'JavaScript/116', 'JavaScript/117', 'JavaScript/120', 'JavaScript/123', 'JavaScript/124', 'JavaScript/125', 'JavaScript/129', 'JavaScript/130', 'JavaScript/132', 'JavaScript/139', 'JavaScript/14', 'JavaScript/145', 'JavaScript/148', 'JavaScript/149', 'JavaScript/152', 'JavaScript/159', 'JavaScript/162', 'JavaScript/163', 'JavaScript/17', 'JavaScript/20', 'JavaScript/21', 'JavaScript/22', 'JavaScript/25', 'JavaScript/26', 'JavaScript/29', 'JavaScript/30', 'JavaScript/32', 'JavaScript/33', 'JavaScript/34', 'JavaScript/37', 'JavaScript/42', 'JavaScript/44', 'JavaScript/49', 'JavaScript/5', 'JavaScript/55', 'JavaScript/58', 'JavaScript/6', 'JavaScript/62', 'JavaScript/63', 'JavaScript/68', 'JavaScript/7', 'JavaScript/70', 'JavaScript/74', 'JavaScript/76', 'JavaScript/8', 'JavaScript/81', 'JavaScript/87', 'JavaScript/88', 'JavaScript/9', 'JavaScript/91', 'JavaScript/95', 'JavaScript/96']
# java_int_specials_ids = ['Java/0', 'Java/10', 'Java/102', 'Java/108', 'Java/109', 'Java/114', 'Java/115', 'Java/121', 'Java/122', 'Java/124', 'Java/126', 'Java/13', 'Java/131', 'Java/132', 'Java/134', 'Java/135', 'Java/138', 'Java/139', 'Java/142', 'Java/144', 'Java/146', 'Java/147', 'Java/150', 'Java/151', 'Java/154', 'Java/157', 'Java/16', 'Java/160', 'Java/18', 'Java/2', 'Java/23', 'Java/24', 'Java/25', 'Java/3', 'Java/31', 'Java/35', 'Java/36', 'Java/39', 'Java/4', 'Java/40', 'Java/41', 'Java/43', 'Java/45', 'Java/46', 'Java/47', 'Java/48', 'Java/49', 'Java/52', 'Java/53', 'Java/54', 'Java/55', 'Java/56', 'Java/57', 'Java/59', 'Java/60', 'Java/61', 'Java/64', 'Java/66', 'Java/67', 'Java/69', 'Java/71', 'Java/72', 'Java/73', 'Java/75', 'Java/76', 'Java/77', 'Java/78', 'Java/80', 'Java/82', 'Java/83', 'Java/85', 'Java/91', 'Java/92', 'Java/94', 'Java/95', 'Java/97', 'Java/98', 'Java/99']
java_int_specials_ids = ['Java/0', 'Java/10', 'Java/102', 'Java/108', 'Java/109', 'Java/114', 'Java/115', 'Java/121', 'Java/122', 'Java/124', 'Java/126', 'Java/13', 'Java/131', 'Java/132', 'Java/133', 'Java/134', 'Java/135', 'Java/138', 'Java/139', 'Java/142', 'Java/144', 'Java/146', 'Java/147', 'Java/150', 'Java/151', 'Java/154', 'Java/157', 'Java/16', 'Java/160', 'Java/18', 'Java/2', 'Java/23', 'Java/24', 'Java/3', 'Java/31', 'Java/35', 'Java/36', 'Java/39', 'Java/4', 'Java/40', 'Java/41', 'Java/43', 'Java/45', 'Java/46', 'Java/47', 'Java/48', 'Java/49', 'Java/52', 'Java/53', 'Java/54', 'Java/55', 'Java/56', 'Java/57', 'Java/59', 'Java/60', 'Java/61', 'Java/63', 'Java/64', 'Java/66', 'Java/67', 'Java/69', 'Java/71', 'Java/72', 'Java/73', 'Java/75', 'Java/76', 'Java/77', 'Java/78', 'Java/80', 'Java/82', 'Java/83', 'Java/85', 'Java/91', 'Java/92', 'Java/94', 'Java/95', 'Java/97', 'Java/98', 'Java/99']
def generate_run_test_java(code, entry_point, task_inputs, orgmain, task_id):
    braces = "{}"
    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]
    sub_test_cases = list(divide_chunks(task_inputs, 50))
    main = "public class Main {\n" + create_map_string

    for chunk_number in range(len(sub_test_cases)):
        main += f"\tpublic static void test{chunk_number}()  throws NoSuchAlgorithmException {braces[0]}\n\t\tSolution s = new Solution();\n\t\tSolutionGenerated s2 = new SolutionGenerated();\n\t\tList<Boolean> correct = Arrays.asList(\n\t\t\t"
        if task_id in java_int_specials_ids:
            main += ",\n\t\t\t".join([f"s.{entry_point}({i}) == s2.{entry_point}({i})" for i in sub_test_cases[chunk_number]])
        else:
            main += ",\n\t\t\t".join([f"s.{entry_point}({i}).equals(s2.{entry_point}({i}))" for i in sub_test_cases[chunk_number]])
        main += "\n\t\t);\n\t\tif (correct.contains(false)) {\n\t\t\tthrow new AssertionError();\n\t\t}\n\t}\n"

    main += "\tpublic static void main(String[] args) throws NoSuchAlgorithmException {\n"
    for chunk_number in range(len(sub_test_cases)):
        main += f"\t\ttest{chunk_number}();\n"
    main += "\t}\n}\n"

    # "\tpublic static void main(String[] args) throws NoSuchAlgorithmException {\n\t\tSolution s = new Solution();\n\t\tSolutionGenerated s2 = new SolutionGenerated();\n\t\tList<Boolean> correct = Arrays.asList(\n\t\t\t"
    # if task_id in java_int_specials_ids:
    #     main += ",\n\t\t\t".join([f"s.{entry_point}({i}) == s2.{entry_point}({i})" for i in task_inputs])
    # else:
    #     main += ",\n\t\t\t".join([f"s.{entry_point}({i}).equals(s2.{entry_point}({i}))" for i in task_inputs])
    # main += "\n\t\t);\n\t\tif (correct.contains(false)) {\n\t\t\tthrow new AssertionError();\n\t\t}\n\t}\n}"
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
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplus_dir}/java/{folder_name}"):
       os.mkdir(f"/home/frabbi/Desktop/{evalplus_dir}/java/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplus_dir}/java/{folder_name}/Main.java", "w") as f:
        f.write(main)
    # with open(f"/home/frabbi/Desktop/{evalplus_dir}/java/{folder_name}/Solution.java", "w") as f:
    #     f.write(code)

with open("cpp_helper.txt", "r") as f:
    cpp_tostring = f.read()
def generate_run_test_cpp(code, entry_point, task_inputs, orgmain, task_id):
    # generatedMethodName
    # assert (has_close_elements({1.0, 2.0, 5.9, 4.0, 5.0}, 0.95) == true);
    main = "#undef NDEBUG\n#include<assert.h>\n#include <iostream>\nusing namespace std;\nint main(){\n"
    for i in task_inputs:
        # main += f"\tassert (toString({entry_point}({i})) == toString(generatedMethodName({i})));\n"
        main += f"\tassert ({entry_point}({i}) == generatedMethodName({i}));\n"
        # main += f"\tcout << \"#\";\n"
    main += "}"
    main = cpp_tostring +"\n"+ main + "\n"
    full_code = code + "\n" + main
    full_code = "###GENERATEDCODE###\n" + full_code

    folder_name = task_id.replace("/", "")
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplus_dir}/cpp/{folder_name}"):
        os.mkdir(f"/home/frabbi/Desktop/{evalplus_dir}/cpp/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplus_dir}/cpp/{folder_name}/main.cpp", "w") as f:
        f.write(full_code)
    executable_code = full_code.replace("###GENERATEDCODE###",code.replace(entry_point, "generatedMethodName"));
    with open(f"/home/frabbi/Desktop/{evalplus_dir}/cpp/{folder_name}/fullcode.cpp", "w") as f:
        f.write(executable_code)
    return 0

with open("js_helper.txt", "r") as f:
    js_tostring = f.read()
def generate_run_test_js(code, entry_point, task_inputs, orgmain, task_id):
    main = js_tostring + "\n"
    for i in task_inputs:
        if task_id in js_obj_special_ids:
            main += f"console.assert(toString({entry_point}({i})) == toString(generatedMethodName({i})));\n"
        else:
            main += f"console.assert({entry_point}({i}) == generatedMethodName({i}));\n"

    generated_code_template = "###GENERATEDCODE###\n"
    full_code = generated_code_template + "\n" + code + "\n" + main + "\n"

    folder_name = task_id.replace("/", "")
    if not os.path.exists(f"/home/frabbi/Desktop/{evalplus_dir}/js/{folder_name}"):
        os.mkdir(f"/home/frabbi/Desktop/{evalplus_dir}/js/{folder_name}")
    with open(f"/home/frabbi/Desktop/{evalplus_dir}/js/{folder_name}/main.js", "w") as f:
        f.write(full_code)
    executable_code = full_code.replace("###GENERATEDCODE###", code.replace(entry_point, "generatedMethodName"));
    with open(f"/home/frabbi/Desktop/{evalplus_dir}/js/{folder_name}/fullcode.js", "w") as f:
        f.write(executable_code)


def generate_output(prompts, inputs, lang):
    print(lang)
    timeStarted = time.time()
    for prompt in prompts:
        task_id = prompt["task_id"]
        task_inputs = inputs[task_id]
        solution = prompt["prompt"] + prompt["canonical_solution"]
        if lang == "js":
            if task_id in ['JavaScript/39', 'JavaScript/163', 'JavaScript/44', 'JavaScript/49', 'JavaScript/55', 'JavaScript/63', 'JavaScript/76', 'JavaScript/91', 'JavaScript/95']:
                continue
            # if task_id in ['JavaScript/111', 'JavaScript/124', 'JavaScript/132', 'JavaScript/139', 'JavaScript/162', 'JavaScript/163', 'JavaScript/39', 'JavaScript/44', 'JavaScript/49', 'JavaScript/55', 'JavaScript/63', 'JavaScript/76', 'JavaScript/91', 'JavaScript/95']:
            #     continue
            generate_run_test_js(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)
        if lang == "cpp":
            if task_id in ['CPP/110', 'CPP/115', 'CPP/123', 'CPP/137', 'CPP/15', 'CPP/163', 'CPP/18', 'CPP/22', 'CPP/28', 'CPP/32', 'CPP/33', 'CPP/34', 'CPP/38', 'CPP/39', 'CPP/44', 'CPP/46', 'CPP/49', 'CPP/50', 'CPP/55', 'CPP/58', 'CPP/63', 'CPP/74', 'CPP/76', 'CPP/87', 'CPP/95']:
                continue
            # if task_id in ["CPP/10", "CPP/15", "CPP/18", "CPP/22", "CPP/32", "CPP/34", "CPP/38", "CPP/46", "CPP/50", "CPP/58", "CPP/63", "CPP/95", "CPP/123"]:
            #     continue
            generate_run_test_cpp(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)
        if lang == "java":
            if task_id in ['Java/123', 'Java/133', 'Java/144', 'Java/22', 'Java/25', 'Java/32', 'Java/33', 'Java/34', 'Java/55', 'Java/58', 'Java/63', 'Java/76', 'Java/78', 'Java/87']:
                continue
            # if task_id in ["Java/25", "Java/32", "Java/34", "Java/58", "Java/87", "Java/133", "Java/55", "Java/63", "Java/91"]:
            #     continue
            generate_run_test_java(solution, prompt["entry_point"], task_inputs, prompt["test"], task_id)
    print(str(time.time()-timeStarted))
# prompt = java_prompts[0]
# inputs = java_inputs[prompt["task_id"]]
# lang = "java"

evalplus_dir = "evalplus_all"

# generate_output(java_prompts, java_inputs, "java")
# print("="*50)
# print("="*50)
generate_output(js_prompts, js_inputs, "js")
# generate_output(cpp_prompts, cpp_inputs, "cpp")
# generate_output(java_prompts, java_inputs, "java")


# def generate_test_(lang):
#     inputs = {"java":java_inputs, "cpp":cpp_inputs, "js":js_inputs}[lang]

