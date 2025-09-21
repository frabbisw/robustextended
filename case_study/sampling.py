import sys
import os
import json

model = sys.argv[1]
lang = sys.argv[2]
scope = sys.argv[3]

all_lines = []

perturb_dir = f"../datasets/{model}/generated_pass5_1/{lang}/{scope}"
# datasets/magicoder7b/generated_pass5_1/cpp/format/tab_indent/f_s
for method in os.listdir(perturb_dir):
    for file_name in os.listdir(os.path.join(perturb_dir, method)):
        if file_name.startswith("f_") and file_name.endswith(".jsonl"):
            with open(os.path.join(perturb_dir, method, file_name), "r") as f:
                all_lines += f.readlines()

print(len(all_lines))
