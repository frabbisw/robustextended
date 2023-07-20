import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import ast
import re
from collections import Counter
def identify_argument_types(func_call_string):
    tree = ast.parse(func_call_string)
    func_call = tree.body[0].value

    if isinstance(func_call, ast.Call):
        arguments = func_call.args

        arg_types = []
        for arg in arguments:
            arg_type = type(eval(ast.unparse(arg)))
            arg_types.append(arg_type)

        return arg_types

    return []
def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts
def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)
def add_slashes(input_string):
    return input_string.replace("\r","\\r").replace("\n","\\n").replace("\\","\\\\").replace("\t","\\t").replace("\"","\\\"")
    rets = ""
    for s in input_string:
        if s in ["\"", "\\"]:
            rets += "\\" + s
        else:
            rets += s
    return rets
# MAX_LIST_SIZE = 100
def recurse(line, lang):
    if line is None:
        return {"java":"null","cpp":"NULL","js":"null"}[lang]
    if isinstance(line, bool):
        if lang in ["java", "cpp", "js"]:
            return str(int(line))
    if isinstance(line, list):
        # line = line[:MAX_LIST_SIZE]
        converted = []
        for l in line:
            converted.append(recurse(l, lang))
        if lang == "java":
            return f"new ArrayList<>(Arrays.asList({', '.join(converted)}))"
        if lang == "cpp":
            return "{" + ", ".join(converted) + "}"
        if lang == "js":
            return "[" + ", ".join(converted) + "]"
    elif isinstance(line, str):
        return f"\"{add_slashes(line)}\""
    elif isinstance(line, int):
        if line > 147483646:
            return "147483646"
        elif line < -147483646:
            return "-147483646"
        return str(line)
    elif isinstance(line, float):
        if line > 147483646:
            return "147483646.0"
        elif line < -147483646:
            return "-147483646.0"
        return str(line)
    elif isinstance(line, dict):
        if lang == "java":
            ks = []
            vs = []
            for k in line.keys():
                v = line[k]
                ks.append(recurse(k,lang))
                vs.append(recurse(v,lang))
            javakeys = f"new ArrayList<>(Arrays.asList({', '.join(ks)}))"
            javavalues = f"new ArrayList<>(Arrays.asList({', '.join(vs)}))"
            return f"createMap({javakeys}, {javavalues})"
        if lang == "cpp":
            cppdict = []
            for k in line.keys():
                v = line[k]
                cppdict.append(f"{{{recurse(k, lang)}, {recurse(v, lang)}}}")
            return "{" + ", ".join(cppdict) + "}"
        if lang == "js":
            jsdict = []
            for k in line.keys():
                v = line[k]
                jsdict.append(f"{recurse(k,lang)}: {recurse(v,lang)}")
            return "{" + ", ".join(jsdict) + "}"
        return str(line)
    else:
        print(f"{type(line)} type not supported")
        # print(line)
        return "#####"

def py_to_others(line, lang):
    if line is None:
        return {"java":"null","cpp":"NULL","js":"null"}[lang]
    line_mod = []
    for l in line:
        line_mod.append(recurse(l, lang))
    return ", ".join(line_mod)

evalplus_type = "full"
python_prompts = load_prompts(f"/home/frabbi/Documents/evalplus/{evalplus_type}.jsonl")
task_id_map = {"java":"Java", "cpp":"CPP", "js":"JavaScript"}

def get_input_dict(lang):
    inputs_dict = {}
    for prompt in python_prompts:
        task_id = prompt["task_id"]
        task_id = task_id.replace("HumanEval",task_id_map[lang])
        test_cases_py = prompt['plus_input']
        test_cases_others = []
        for tc in test_cases_py:
            to = py_to_others(tc,lang)
            test_cases_others.append(to)
        inputs_dict[task_id] = test_cases_others
    return inputs_dict

def cast_list(lst, type):
    if not isinstance(lst, list):
        return list(lst)
    ret_lst = []
    for item in lst:
        if item == None:
            ret_lst.append(None)
        else:
            try:
                casted = type(item)
            except:
                casted = str(item)
            ret_lst.append(casted)
    return ret_lst
def detect_list_type(lst):
    if len(lst) == 0:
        return "empty_list"
    for item in lst:
        if isinstance(item, str):
            return str
        if isinstance(item, float):
            return float
        if isinstance(item, int):
            return int
    return "mixed"

def filter_python_prompt(prompt):
    test_cases_py = prompt['plus_input']
    # test_cases_py = test_cases_py[:min(len(test_cases_py), MAX_LIST_SIZE)]
    case_types = {}
    for i in range(len(test_cases_py)):
        tc = test_cases_py[i]
        for j in range(len(tc)):
            sample = tc[j]
            if j not in case_types.keys():
                case_types[j] = []
            case_type = eval(type(sample).__name__)
            # if case_type == list:
            #     case_type = detect_list_type(sample)
            case_types[j].append(case_type)
    # print(case_types)
    for j in case_types.keys():
        if 0 == case_types[j].count(list):
            if case_types[j].count(int) + case_types[j].count(float) + case_types[j].count(None) == len(case_types[j]):
                if case_types[j].count(int) < case_types[j].count(float):
                    for i in range(len(test_cases_py)):
                        test_cases_py[i][j] = float(test_cases_py[i][j])
                else:
                    for i in range(len(test_cases_py)):
                        test_cases_py[i][j] = int(test_cases_py[i][j])
            continue
        if 0 < case_types[j].count(list) < len(case_types[j]):
            for i in range(len(test_cases_py)):
                test_cases_py[i][j] = list(test_cases_py[i][j])
        list_types = [detect_list_type(test_cases_py[i][j]) for i in range(len(test_cases_py))]
        if list_types.count(int) + list_types.count(float) + list_types.count("empty_list") == len(case_types[j]):
            if list_types.count(float) > list_types.count(int):
                for i in range(len(test_cases_py)):
                    test_cases_py[i][j] = cast_list(test_cases_py[i][j],float)
            else:
                for i in range(len(test_cases_py)):
                    test_cases_py[i][j] = cast_list(test_cases_py[i][j],int)
        # print(list_types.count(int), list_types.count(float), list_types.count("empty_list"), len(case_types[j]))

    # print(prompt['plus_input'])
    prompt['plus_input'] = test_cases_py

# for prompt in python_prompts:
    # if prompt["task_id"] == "HumanEval/2":
    # if prompt["task_id"] == "HumanEval/20":
        # print(prompt['plus_input'])
    # if prompt["task_id"] == "HumanEval/20":
    # filter_python_prompt(prompt)
    # if prompt["task_id"] == "HumanEval/20":
    #     print(prompt["plus_input"])
# print(prompt['plus_input'])
    # if prompt["task_id"] == "HumanEval/20":
    #     prompt["plus_input"]

def filter_inputs():
    for prompt in python_prompts:
        # if prompt["task_id"] == "HumanEval/157":
        filter_python_prompt(prompt)
filter_inputs()
java_inputs = get_input_dict("java")

with open(f"java_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(java_inputs, f)

cpp_inputs = get_input_dict("cpp")
with open(f"cpp_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(cpp_inputs, f)

js_inputs = get_input_dict("js")
with open(f"js_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(js_inputs, f)

    # print(len(types[key_with_max_values]), types[key_with_max_values])
        # print(len(types[key_with_max_values]))
# filter_inputs("java")

# task_id = "HumanEval/8"
# for prompt in python_prompts:
#     if prompt["task_id"] == task_id:
#         print(prompt["plus_input"])

# print(java_inputs)
# cpp_inputs = get_input_dict("cpp")
# js_inputs = get_input_dict("js")

# with open(f"cpp_inputs_{evalplus_type}", "wb") as f:
#     pickle.dump(cpp_inputs, f)
# with open(f"js_inputs_{evalplus_type}", "wb") as f:
#     pickle.dump(js_inputs, f)
