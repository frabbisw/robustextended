import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys

def load_prompts(filename):
    prompts = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            prompts[prompt['task_id']]=prompt

    return prompts
def save_prompts(filename, prompts):
    if isinstance(prompts, list):
        with jsonlines.open(filename, mode='w') as writer:
            for line in prompts:
                jsonlines.Writer.write(writer, line)
    elif isinstance(prompts, dict):
        tmp = []
        for task_id in prompts.keys():
            tmp.append(prompts[task_id])
        # print(tmp)
        with jsonlines.open(filename, mode='w') as writer:
            for line in tmp:
                jsonlines.Writer.write(writer, line)

#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
models_dict = {"codegen6bmulti": "Salesforce/codegen-6B-multi", "codegen2bmulti": "Salesforce/codegen-2B-multi", "incoder1b": "facebook/incoder-1B", "incoder6b": "facebook/incoder-6B"}

checkpoint = models_dict[sys.argv[2]]

code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"])

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1536,temperature=0.2,top_p=0.95,do_sample = True)
    code = code_generaton_tokenizer.decode(completion[0])
    return code

filepath = sys.argv[1]
prompts = load_prompts(filepath)

ids = []
if "/java/" in filepath:
    ids = ['Java/31', 'Java/55', 'Java/63']
elif "/cpp/" in filepath:
    ids = ['CPP/31', 'CPP/39', 'CPP/44', 'CPP/49', 'CPP/55', 'CPP/63', 'CPP/76', 'CPP/91', 'CPP/96', 'CPP/124', 'CPP/125', 'CPP/127', 'CPP/132', 'CPP/139']
elif "/js/" in filepath:
    ids = ['JavaScript/32', 'JavaScript/39', 'JavaScript/44', 'JavaScript/49', 'JavaScript/55', 'JavaScript/63', 'JavaScript/76', 'JavaScript/91', 'JavaScript/96', 'JavaScript/124', 'JavaScript/125', 'JavaScript/127', 'JavaScript/132', 'JavaScript/139']

for task_id in ids:
    prompts[task_id]["gc"] = prompt_to_code(prompts[task_id]["prompt"])
save_prompts(filepath, prompts)
print("saved", filepath)

# print(prompt_to_code(prompts[0]["prompt"]))

# print(sys.argv[1], sys.argv[2])