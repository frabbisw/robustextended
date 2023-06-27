import os
import subprocess

# dataset_names = ['humanevalpy', 'humanevaljava', 'humanevalcpp', 'humanevaljs', 'humanevalgo']
dataset_names = ['humanevalcpp', 'humanevaljs', 'humanevaljava']
# methods = ["nlaugmenter", "natgen", "format", "func_name"]
# methods = ["nlaugmenter", "format", "func_name", "natgen"]
methods = ["format"]
aug_methods = {"nlaugmenter": 10, "natgen": 6, "format": 6, "func_name": 6}
K = 5
template = "python perturb_multi.py --data {dataset} --method {method} --aug_method {aug_method} --seed {seed} {extra}"

for d in dataset_names:
    for m in methods:
        for a in range(aug_methods[m]):
            for k in range(K):
                command = template.format(dataset = d, method = m, aug_method = a, seed = k, overwrite = True, extra = "--task partial_code" if m in ["natgen", "format"] else "")
                print(command)
                # # print(command.split())
                # output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT)
                # print(output.decode('utf-8'))