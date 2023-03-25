import json
import os
import jsonlines
from tqdm import tqdm as tq

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

java_path = "../datasets/nominal/HumanEval_java.jsonl"
cpp_path = "../datasets/nominal/HumanEval_cpp.jsonl"
py_path = "../datasets/nominal/HumanEval_py.jsonl"
go_path = "../datasets/nominal/HumanEval_go.jsonl"
js_path = "../datasets/nominal/HumanEval_js.jsonl"


#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
##code generation model
# checkpoint = "Salesforce/codegen-2B-mono"
model_name = "codegen-6B-multi"
checkpoint = "Salesforce/"+model_name
code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1536,temperature=0.8,top_p=0.9,do_sample = True)
    return code_generaton_tokenizer.decode(completion[0])

prompts = load_prompts("../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s0.jsonl")
save_dir = f"../datasets/generated/java/docstring"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for itr in range(10):
    for i in tq(range(len(prompts))):
        p = prompts[i]
        p["gc"] = prompt_to_code(p["prompt"])
        prompts[i] = p
    save_prompts(os.path.join(save_dir, f"humanevaljava_SynonymInsertion_s0_java_6B_{itr}.jsonl"), prompts)
    print("saved", os.path.join(save_dir, f"humanevaljava_SynonymInsertion_s0_java_6B_{itr}.jsonl"))
print("saved all files")

