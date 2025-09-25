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
    lines = [line.strip() for line in lines if line.strip() != ""] + ["\n"] 
    print("*******")
    print(nl)
    if "```" not in nl:
        return "\n".join(lines)
    lines = [lines[i] for i in range(len(lines)-1) if "```" not in lines[i+1]]
    nl = "\n".join(lines)
    print("*******")
    print(nl)
    print("*******")
    nl = nl[len(("```"))+nl.find("```"):nl.rfind("```")]
    return nl

def filter_gc(gc):
    stop_tokens = [["<｜begin▁of▁sentence｜>", "<｜end▁of▁sentence｜>"], ["<|endoftext|>", "<|endoftext|>"], ["<code>", "</code>"], ["<|im_start|>", "<|im_end|>"]]
    for st, et in stop_tokens:
        if st in gc:
            gc = gc[gc.find(st)+len(st):]
        if et in gc:
            gc = gc[:gc.find(et)]
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
<｜begin▁of▁sentence｜>You are a text rewriter.
    Rewrite the instruction below by fixing grammar and spelling, improving readability, and ensuring smooth flow.
    Output only the improved instruction text — no extra words, no code blocks.

    Instruction:
GiVEn a sTrinG text, replace ALL sPaces in IT WIth uNderscores,
And if a string has moRE tHaN 2 cOnsecutIVe spAces,
ThEn REpLacE All cOnSeCuTiVE sPAceS wITH -

fiX_SPaces("Example") == "Example"
fix_spaces("Example 1") == "Example_1"
fix_spaces(" Example 2") == "_Example_2"
fix_spaces(" Example   3") == "_Example-3"


    Improved Instruction:

Given a string text, replace all spaces in it with underscores.
If a string has more than 2 consecutive spaces, then replace all consecutive spaces with -.

Here is a Python function that implements this:

```python
def fix_spaces(text):
    return text.replace(' ', '_').replace('__', '-').replace('---', '-').replace('----', '-')
```

This function works by first replacing all single spaces with underscores. Then it replaces all double underscores with a single dash, and so on, up to four dashes. This ensures that if there are more than two consecutive spaces, they are replaced with a single dash.<｜end▁of▁sentence｜>
'''

filter_gc(sample)

# for i, prompt in enumerate(prompts):
#     print(prompt["processed_nl"])
#     print("-"*50)
#     processed_nl = filter_gc(prompt["processed_nl"])
#     processed_nl = processed_nl[processed_nl.find("Improved Instruction:")+len("Improved Instruction:"):]
#     print(processed_nl)
#     print("=="*50)
#     prompts[i]["processed_prompt"] = replace_docstring(processed_nl, prompt, lang)
#     # print(prompts[i])
#     # print("="*50)
#     # print("="*50)
    
# save_prompts(filepath, prompts)


