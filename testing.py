import json

prompts = []
with open("datasets/nominal/HumanEval_java.jsonl") as f:
    for line in f.readlines():
        prompts.append(json.loads(line)["prompt"])

