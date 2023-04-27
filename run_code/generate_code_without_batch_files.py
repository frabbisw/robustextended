import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
from pynvml import *


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

#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_name = "codegen-6B-multi"
checkpoint = "Salesforce/"+model_name
code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map = 'auto')
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint, device_map = 'auto')

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt"), max_length=1536,temperature=0.2,top_p=0.95,do_sample = True)
    code = code_generaton_tokenizer.decode(completion[0])
    del code_generaton_model, code_generaton_tokenizer

    torch.cuda.empty_cache()
    return code

prompts = load_prompts(sys.argv[1])
save_dir = sys.argv[2]
ext, _ = sys.argv[1][5:].split(".")

_, ext = ext[-5:].split("_")
#
outpath = os.path.join(save_dir, f"f_{ext}.jsonl")


if not os.path.exists(save_dir):
    os.makedirs(save_dir)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
#
for i in tq(range(len(prompts))):
    p = prompts[i]
    try:
        p["gc"] = prompt_to_code(p["prompt"])
        prompts[i] = p
    except:
        nvmlInit()
        h1 = nvmlDeviceGetHandleByIndex(0)
        h2 = nvmlDeviceGetHandleByIndex(1)
        info1 = nvmlDeviceGetMemoryInfo(h1)
        info2 = nvmlDeviceGetMemoryInfo(h2)

        # print(f'total 1   : {info1.total}')
        print(f'free  1   : {info1.free}')
        # print(f'used  1   : {info1.used}')

        # print(f'total 2   : {info1.total}')
        print(f'free  2   : {info2.free}')
        # print(f'used  2   : {info1.used}')
        exit()
save_prompts(outpath, prompts)
print("saved", outpath)

# print(prompt_to_code(prompts[0]["prompt"]))

# print(sys.argv[1], sys.argv[2])