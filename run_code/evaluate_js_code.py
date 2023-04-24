import json
import pdb
import pickle
from tqdm import tqdm as tq
import os
import subprocess
from collections import Counter
import pandas as pd

def view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"])
    return prompts

def full_view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"]+json.loads(line)["canonical_solution"])
    return prompts

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts



def test_it(code, main, new_entry_point, i):
    code = code[:code.find("<|endoftext|>")]
    old_entry_point = nominal_prompts[i]["entry_point"]
    main = main.replace(old_entry_point, new_entry_point)
    full_code = code + main

    with open("../tmp/Sample.js", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")
    try:
        # run node command to execute full code
        run_output = subprocess.check_output(['node', 'Sample.js'], stderr=subprocess.STDOUT, timeout=3)

        # print the output from the Java program
        print(f"{i} successful")
        print(run_output.decode('utf-8'))
        return 1

    except subprocess.CalledProcessError as e:
        # print the error message and output from the Java compiler or program
        print(f"{i} failed")
        print("An error occurred while running the program:")
        print("*"*50)
        print(code)
        print("*" * 50)
        print(main)
        print("*" * 50)

        print(e.output.decode('utf-8'))
        print("Return code: ", e.returncode)
        # import pdb; pdb.set_trace()
        # print()
        return 0
    except subprocess.TimeoutExpired as e:
        print(f"{i} timeout")
        return 0

nominal_prompts = load_prompts("../datasets/nominal/HumanEval_js.jsonl")
perturbed_prompts = load_prompts("../datasets/generated/js/natgen/VarRenamerRN/f_0.jsonl")


for i in range(164):
    test_it(perturbed_prompts[i]["gc"], perturbed_prompts[i]["test"], perturbed_prompts[i]["entry_point"], i)

import pdb; pdb.set_trace()