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

def test_it(code, main, i):
    full_code = code + main
    with open("../tmp/cpp_code.cpp", "w") as f:
        f.write(full_code)
    os.chdir("../tmp/")

    try:
        # run g++ command to compile Java code
        compile_output = subprocess.check_output(['g++', '-o', 'cpp_code', 'cpp_code.cpp'], stderr=subprocess.STDOUT)

        # run program to execute Main class
        run_output = subprocess.check_output(['./cpp_code'], stderr=subprocess.STDOUT, timeout=3)

        # print the output from the Java program
        print(f"{i} successful")
        print(run_output.decode('utf-8'))

    except subprocess.CalledProcessError as e:
        # print the error message and output from the Java compiler or program
        print(f"{i}failed")
        print("An error occurred while running the program:")
        print(e.output.decode('utf-8'))
        print("Return code: ", e.returncode)
        # import pdb; pdb.set_trace()
        # print()
    except subprocess.TimeoutExpired as e:
        print(f"{i} timeout")

path = "../datasets/nominal/HumanEval_cpp.jsonl"

prompts = load_prompts(path)

for i in range(164):
    test_it(prompts[i]["prompt"]+prompts[i]["canonical_solution"], prompts[i]["test"], i)

# pdb.set_trace()