import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle

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
def recurse(line, lang):
    if line is None:
        return {"java":"null","cpp":"NULL","js":"null"}[lang]
    if isinstance(line, list):
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
        return f"\"{line}\""
    elif isinstance(line, int):
        return str(line)
    elif isinstance(line, float):
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
                cppdict.append(f"{{{recurse(k, lang)}: {recurse(v, lang)}}}")
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

evalplus_type = "mini"
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

java_inputs = get_input_dict("java")
cpp_inputs = get_input_dict("cpp")
js_inputs = get_input_dict("js")

with open(f"java_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(java_inputs, f)
with open(f"cpp_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(cpp_inputs, f)
with open(f"js_inputs_{evalplus_type}", "wb") as f:
    pickle.dump(js_inputs, f)
