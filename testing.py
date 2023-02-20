import json

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

java_path = "datasets/nominal/HumanEval_java.jsonl"
cpp_path = "datasets/nominal/HumanEval_cpp.jsonl"
py_path = "datasets/nominal/HumanEval_py.jsonl"
go_path = "datasets/nominal/HumanEval_go.jsonl"
js_path = "datasets/nominal/HumanEval_js.jsonl"

import pdb; pdb.set_trace()
