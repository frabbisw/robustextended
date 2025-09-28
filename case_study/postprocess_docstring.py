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

def remove_code_snippets(nl):
    lines = nl.split("\n")
    # lines = [line.strip() for line in lines if line.strip() != ""] + ["\n"] 
    lines = [line.strip() for line in lines if "here is" not in line.lower() and "python" not in line.lower()] + ["\n"] 
    # lines = [line.strip() for line in lines] + ["\n"] 
    
    if "```" not in nl:
        return "\n".join(lines)
    lines = [lines[i] for i in range(len(lines)-1) if "```" not in lines[i+1]]
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
    print(gc)
    print("*"*50)
    gc = gc[gc.rfind("Improved Instruction:")+len("Improved Instruction:"):]
    print(gc)
    print("#"*50)
    gc = remove_code_snippets(gc)
    #     gc = gc[:gc.find("```")] + gc[3 + gc.rfind("```"):]
    #     lns = gc.split("\n")
    #     gc = "\n".join([ln if not ln.strip().endswith(":") else "" for ln in lns])
    #     # gc = "\n".join([ln if "python solution" not in ln.lower() or "corrected version" not in ln.lower() else "" for ln in lns])
    #     # gc = gc.strip()
    #     return gc.strip()
    return gc.strip()

def replace_docstring(new_nl, prompt, lang):
    if lang == "cpp":
        start_index = prompt["prompt"].find("/*")
        end_index = prompt["prompt"].find("*/")
        return f"/*{new_nl}*/\n{prompt['prompt'][end_index+2:]}"

sample = '''
<｜begin▁of▁sentence｜>You are an expert code comment writer. 
    Rewrite the coding instruction below by fixing grammar and spelling, improving readability, and ensuring smooth flow. 
    Output only the improved instruction text — no extra words, no code blocks, and don't delete any info.  
    
    Instruction: 
Your task is to find the next vowel between two consonants on the right side of the word (case sensitive), and vowels at the beginning and end do not count. You will return an empty string if you have not found a vowel that meets the above condition, and you can assume that the given string contains only English letters.

Example:
get_closest_vowel("yogurt") ==> "u"
get_closest_vowel("FULL") ==> "U"
get_closest_vowel("quick") ==> ""
get_closest_vowel("ab") ==> ""
  
    
    Improved Instruction: 
    Given a string, find the next vowel that is on the right side of a consonant and return it. If there is no such vowel, return an empty string. The string will only contain English letters and the first and last vowels do not count.<｜end▁of▁sentence｜>
'''

# print(sample)
# print("-"*50)
# gg = filter_gc(sample)
# print(gg)
# print("="*50)

# exit(1)
for i, prompt in enumerate(prompts):
    # print(prompt["processed_nl"])
    # print("-"*50)
    processed_nl = filter_gc(prompt["processed_nl"])
    if len(processed_nl) < 10:
        processed_nl = prompt["processed_nl"]
    print(prompt["processed_nl"])
    print("--"*50)
    print(processed_nl)
    print("=="*50)
    print()
    prompts[i]["processed_prompt"] = replace_docstring(processed_nl, prompt, lang)
    # print(prompts[i])
    # print("="*50)
    # print("="*50)
    
save_prompts(filepath, prompts)


