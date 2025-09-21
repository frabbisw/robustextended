import sys
import os
import json
from random import sample

model = sys.argv[1]
lang = sys.argv[2]
scope = sys.argv[3]

def parse_docstring(prompt, lang):
    pass

all_lines = []
perturb_dir = f"../datasets/{model}/generated_pass5_1/{lang}/{scope}"
# datasets/magicoder7b/generated_pass5_1/cpp/format/tab_indent/f_s
for method in os.listdir(perturb_dir):
    for file_name in os.listdir(os.path.join(perturb_dir, method)):
        if file_name.startswith("f_") and file_name.endswith(".jsonl"):
            with open(os.path.join(perturb_dir, method, file_name), "r") as f:
                all_lines += f.readlines()

sampled_list = sample(all_lines, 368)

for sample in sampled_list:
    print(sample["prompt"])
    print("\n")

os.makedirs(f"../datasets/samples/{model}/{lang}/{scope}", exist_ok=True)
with open(f"../datasets/samples/{model}/{lang}/{scope}/sample_368.jsonl", "w") as f:
    f.write("".join(sampled_list))
    print("saved")

# print(len(all_lines))
