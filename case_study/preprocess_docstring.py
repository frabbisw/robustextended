import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

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

device = "cuda:0" if torch.cuda.is_available() else "cpu"
#models_dict = {"codegen6bmulti": "Salesforce/codegen-6B-multi", "codegen2bmulti": "Salesforce/codegen-2B-multi", "incoder1b": "facebook/incoder-1B", "incoder6b": "facebook/incoder-6B", "magicoder7b": "ise-uiuc/Magicoder-S-DS-6.7B"}
models_dict = {"magicoder7b": "/home/f_rabbi/models/Magicoder-S-DS-6.7B", "qwencoder": "/home/f_rabbi/models/Qwen2.5-Coder-7B-Instruct", "codegen6bmulti": "/home/f_rabbi/models/codegen-6B-multi"}

checkpoint = models_dict[sys.argv[2]]

code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"])

def preprocess_nl(nl):
    # prompt = f"Reply with a corrected version of the following code instruction with all grammatical and spelling errors fixed. If there are no errors, reply with a copy of the original text. \n\n Input Instruction: {nl} \n Corrected Instruction: "
    prompt = f"""You are a text rewriter. 
    Rewrite the instruction below by fixing grammar and spelling, improving readability, and ensuring smooth flow. 
    Output only the improved instruction text — no extra words, no code blocks.  
    
    Instruction: {nl}  
    
    Improved Instruction: """    
    try:
        completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1024,temperature=0.2,top_p=0.95,do_sample = True)
        processed_nl = code_generaton_tokenizer.decode(completion[0])
    except:
        processed_nl = nl
    return processed_nl

prompts = load_prompts(sys.argv[1])

for i in tq(range(len(prompts))):
    p = prompts[i]
    p["processed_nl"] = preprocess_nl(p["nl"])
    # print(f"before====>\n{p['nl']}\nafter====>\n{p['processed_nl']}")
    # print("="*50)
    prompts[i] = p

save_prompts(sys.argv[1], prompts)
print("saved", sys.argv[1])
