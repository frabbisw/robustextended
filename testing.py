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

prompts = load_prompts("datasets/codegen6bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s0.jsonl")
prompt = prompts[0]

import pdb; pdb.set_trace()