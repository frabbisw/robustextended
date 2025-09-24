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

model = sys.argv[1]
lang = sys.argv[2]
scope = sys.argv[3]

filepath = f"../datasets/samples/{model}/{lang}/{scope}/sample_368.jsonl"

prompts = load_prompts(filepath)

def filter_gc(gc):
    stop_tokens = [["<｜begin▁of▁sentence｜>", "<｜end▁of▁sentence｜>"], ["<|endoftext|>", "<|endoftext|>"], ["<code>", "</code>"], ["<|im_start|>", "<|im_end|>"]]
    for st, et in stop_tokens:
        if st in gc:
            gc = gc[gc.find(st)+len(st):]
        if et in gc:
            gc = gc[:gc.find(et)]
    if "```" in gc:
        gc = gc[:gc.find("```")] + gc[3 + gc.rfind("```"):]
        lns = gc.split("\n")
        gc = "\n".join([ln if not ln.strip().endswith(":") else "" for ln in lns])
        # gc = "\n".join([ln if "python solution" not in ln.lower() or "corrected version" not in ln.lower() else "" for ln in lns])
        # gc = gc.strip()
        return gc.strip()
    return gc.strip()

def replace_docstring(new_nl, prompt, lang):
    if lang == "cpp":
        start_index = prompt["prompt"].find("/*")
        end_index = prompt["prompt"].find("*/")
        return f"/*{new_nl}*/\n{prompt['prompt'][end_index+2:]}"
      
for i, prompt in enumerate(prompts):
    processed_nl = filter_gc(prompt["processed_nl"])
    processed_nl = processed_nl[processed_nl.find("Corrected Instruction: ")+len("Corrected Instruction: "):]
    print(processed_nl)
    print("-"*50)
    prompts[i]["processed_prompt"] = replace_docstring(processed_nl, prompt, lang)
    # print(prompts[i])
    # print("="*50)
    # print("="*50)
    
save_prompts(filepath, prompts)
