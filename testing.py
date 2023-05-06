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

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_name = "codegen-350M-multi"
checkpoint = "Salesforce/"+model_name
code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# Create input tensor and attention mask
input_ids = torch.tensor([[1, 2, 3]]).to(device)

# Print the list of model outputs
outputs = code_generaton_model(input_ids=input_ids, output_attentions=True, return_dict=True,)

import pdb; pdb.set_trace()

# Set up input sentence
input_sentence = "write a cpp code to add two integers."

# Encode input sentence using the tokenizer
input_ids = code_generaton_tokenizer.encode(input_sentence, return_tensors="pt").to(device)

# Generate output sequence and attention weights
output = code_generaton_model.generate(input_ids=input_ids, max_length=512, output_attentions=True)
generated_sequence = output[0]
attention_weights = output[-1]

# Extract attention weights for input sentence
input_tokens = code_generaton_tokenizer.tokenize(input_sentence)
start_idx = 0
for i in range(len(input_tokens)):
    if code_generaton_tokenizer.decode(input_ids[0][i]).strip() == input_tokens[i]:
        start_idx = i
        break
end_idx = start_idx + len(input_tokens)

import pdb; pdb.set_trace()

attention_weights_for_input = attention_weights[0, :, start_idx:end_idx, :]

# Print attention weights for input sentence
print("Attention weights for input sentence:")
print(attention_weights_for_input)