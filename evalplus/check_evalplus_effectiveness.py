import json
import os
import pathlib
def load_prompts(filename):
    prompts = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            prompts[prompt['task_id']]=prompt
    return prompts

before_evalplus = "/home/frabbi/Desktop/backup_old_files/datasets_before_evalplus"
# after_evalplus = "/home/frabbi/Desktop/backup_old_files/datasets_after_evalplus"

# models = ["codegen2bmulti", "codegen6bmulti", "incoder1b", "1ncoder6b"]
models = ["codegen2bmulti"]
results = {}
for model in models:
    paths_he = pathlib.Path(os.path.join(before_evalplus, model))
    for path in list(paths_he.rglob("*")):
        gc_path = str(path)
        ep_path = gc_path.replace("datasets_before_evalplus", "datasets_after_evalplus")
        path_short = gc_path.replace("/home/frabbi/Desktop/backup_old_files/datasets_before_evalplus/","")
        print(path_short)

        if os.path.isfile(gc_path):
            results[path_short]=[]
            prompts_he = load_prompts(gc_path)
            prompts_ep = load_prompts(ep_path)

            for task_id in prompts_he.keys():
                try:
                    if prompts_ep[task_id]["passed"] == 0 and prompts_he[task_id]["passed"] == 1:
                        results[path_short].append(task_id)
                except:
                    print(gc_path, ep_path)
for path_short in results.keys():
    print(path_short, results[path_short])