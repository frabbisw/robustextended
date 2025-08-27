#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
#models_dict = {"codegen6bmulti": "Salesforce/codegen-6B-multi", "codegen2bmulti": "Salesforce/codegen-2B-multi", "incoder1b": "facebook/incoder-1B", "incoder6b": "facebook/incoder-6B", "magicoder7b": "ise-uiuc/Magicoder-S-DS-6.7B"}
models_dict = {"codegen6bmulti": "/home/f_rabbi/models/codegen-6B-multi", "magicoder7b": "/home/f_rabbi/code_trans/models/Magicoder-S-DS-6.7B"}

# checkpoint = models_dict[sys.argv[1]]
checkpoint = models_dict["codegen6bmulti"]

code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"])

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1536,temperature=0.2,top_p=0.95,do_sample = True)
    code = code_generaton_tokenizer.decode(completion[0])
    return code

prompt = '''
# C++
#include <iostream>
using namespace std;

// Function to calculate factorial of a number
int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

#Python
def factorial(n):
'''

cpp_code = prompt_to_code(prompt)

print(cpp_code)
