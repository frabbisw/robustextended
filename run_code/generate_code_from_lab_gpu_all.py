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

#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

device = f"cuda:{sys.argv[4]}" if torch.cuda.is_available() else "cpu"
models_dict = {"codegen6bmulti": "Salesforce/codegen-6B-multi", "codegen2bmulti": "Salesforce/codegen-2B-multi", "incoder1b": "facebook/incoder-1B"}

checkpoint = models_dict[sys.argv[3]]

code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"])

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1536,temperature=0.2,top_p=0.95,do_sample = True)
    code = code_generaton_tokenizer.decode(completion[0])
    return code

prompts = load_prompts(sys.argv[1])
save_dir = sys.argv[2]

try:
    ext = sys.argv[1][5:].split(".")[0]
    ext = ext[-5:].split("_")[-1]
    outpath = os.path.join(save_dir, f"f_{ext}.jsonl")
except:
    if "nominal" in sys.argv[1].lower():
        outpath = os.path.join(save_dir, f"nominalf_0.jsonl")
    elif "partial" in sys.argv[1].lower():
        outpath = os.path.join(save_dir, f"partial_0.jsonl")
    else:
        outpath = os.path.join(save_dir, f"filef_000.jsonl")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
#
for i in tq(range(len(prompts))):
    p = prompts[i]
    p["gc"] = prompt_to_code(p["prompt"])
    prompts[i] = p
save_prompts(outpath, prompts)
print("saved", outpath)

# print(prompt_to_code(prompts[0]["prompt"]))

# print(sys.argv[1], sys.argv[2])