import sys
import os
import json
from random import sample
import jsonlines

filepath = sys.argv[1]
lang = sys.argv[2]

def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

def parse_docstring(prompt, lang):
    if lang in ["cpp", "js", "java"]:
        start_index = prompt.find("/**")
        l_s = len("/**")
        if start_index < 0:
            start_index = prompt.find("/*")
            l_s = len("/*")
        end_index = prompt.find("**/")
        e_s = len("**/")
        if end_index < 0:
            end_index = prompt.find("*/")
            e_s = len("*/")
        if end_index < 0:
            end_index = prompt.find("* /")
            e_s = len("* /")        
        return prompt[start_index + l_s: end_index], start_index, end_index+e_s

prompts = load_prompts(filepath)

for sample in prompts:
    nl, s_l, e_l = parse_docstring(sample["prompt"], lang)
    # print(nl)
    sample["nl"] = nl
    sample["s_l"] = s_l
    sample["e_l"] = e_l
    # print("="*50)

save_prompts(filepath, prompts)

# with open(f"../datasets/samples/{model}/{lang}/{scope}/sample_368.jsonl", "w") as f:
#     f.write("".join(sampled_list))
#     print("saved")

# print(len(all_lines))
