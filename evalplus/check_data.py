import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys

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

prompts = load_prompts("/home/frabbi/Documents/evalplus/full.jsonl")

def py_to_others(line, lang):
    # print(type(line))
    if isinstance(line, list):
        converted = []
        for l in line:
            converted.append(py_to_others(l, lang))
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
    else:
        print(f"{type(line)} type not supported")
        return "#####"

# py_to_others(.9)


for prompt in prompts:
    line = prompt['plus_input'][0]
    # print(hh, type(hh))
    print("*"*50)
    print(line)
    line_mod = []
    for l in line:
        line_mod.append(py_to_others(l, "js"))
    line_mod = ", ".join(line_mod)
    if "#####" in line_mod:
        print("task_id", prompt["task_id"])
        print(prompt["prompt"])
        print(prompt["test"])
    print(line_mod)
    print("*" * 50)
    # break


codes = load_prompts("../datasets/codegen6bmulti_old/generated_pass5_1/java/nominal/f_s0.jsonl")
for code in codes:
    if code["task_id"] == "Java/95":
        print(code["prompt"])
        print(code["test"])
        print(code["task_id"])
# for code in codes:
#     print("*"*50)
#     print(code["test"])
#     print(code["prompt"])
#     print("*" * 50)