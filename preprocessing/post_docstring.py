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

filepath = sys.argv[1]
lang = sys.argv[2]

prompts = load_prompts(filepath)

def remove_code_snippets(nl):
    lines = nl.split("\n")
    # lines = [line.strip() for line in lines if line.strip() != ""] + ["\n"] 
    lines = [line.strip() for line in lines if "here is a" not in line.lower() and "here is an" and "here is the" not in line.lower()] + ["\n"] 
    # lines = [line.strip() for line in lines] + ["\n"] 
    
    if "```" not in nl:
        return "\n".join(lines)
    # lines = [lines[i] for i in range(len(lines)-1) if "```" not in lines[i+1]]
    nl = "\n".join(lines)
    nl = nl[:nl.find("```")] + nl[len(("```"))+nl.rfind("```"):]
    nl = nl.replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n")
    return nl

def filter_gc(gc):
    stop_tokens = [["<｜begin▁of▁sentence｜>", "<｜end▁of▁sentence｜>"], ["<|endoftext|>", "<|endoftext|>"], ["<code>", "</code>"], ["<|im_start|>", "<|im_end|>"]]
    for st, et in stop_tokens:
        if st in gc:
            gc = gc[gc.find(st)+len(st):]
        if et in gc:
            gc = gc[:gc.find(et)]
    # print(gc)
    # print("*"*50)
    # gc = gc[gc.rfind("Improved Instruction:")+len("Improved Instruction:"):]
    gc = gc[gc.rfind("Fixed Text:")+len("Fixed Text:"):]
    gc = gc.replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n")
    # print(gc)
    # print("#"*50)
    if "python```" in gc or "```Python":
        gc = remove_code_snippets(gc)
    # print(gc)
    # print("@"*50)
    #     gc = gc[:gc.find("```")] + gc[3 + gc.rfind("```"):]
    #     lns = gc.split("\n")
    #     gc = "\n".join([ln if not ln.strip().endswith(":") else "" for ln in lns])
    #     # gc = "\n".join([ln if "python solution" not in ln.lower() or "corrected version" not in ln.lower() else "" for ln in lns])
    #     # gc = gc.strip()
    #     return gc.strip()
    return gc.strip()

def replace_docstring(new_nl, prompt, lang, s_l, e_l):
    if lang in ["cpp", "js", "java"]:
        if lang in ["java"]:
            new_nl = "\n".join(["    " + l if not l.startswith("    ") else l for l in new_nl.split("\n")])
            processed_prompt = f"{prompt[:s_l]}/*\n{new_nl}\n    */{prompt[e_l:]}"
        else:
            processed_prompt = f"{prompt[:s_l]}/*\n{new_nl}\n*/{prompt[e_l:]}"
        return processed_prompt

for i, prompt in enumerate(prompts):
    processed_nl = filter_gc(prompt["processed_nl"])
    if len(processed_nl) < 10:
        processed_nl = prompt["nl"]
    prompts[i]["filtered_nl"] = processed_nl
    prompts[i]["processed_prompt"] = replace_docstring(processed_nl, prompt["prompt"], lang, prompt["s_l"], prompt["e_l"])
    
save_prompts(filepath, prompts)


