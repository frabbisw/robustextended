import json
import os
import jsonlines

dataset_dir = "datasets/nominal"
python_dir = "datasets/nominal/humaneval-x/data/python/data"
java_dir = "datasets/nominal/humaneval-x/data/java/data"
cpp_dir = "datasets/nominal/humaneval-x/data/cpp/data"
go_dir = "datasets/nominal/humaneval-x/data/go/data"
js_dir = "datasets/nominal/humaneval-x/data/js/data"
def add_entry_points(dir, lang):
    lines = []
    with open(os.path.join(dir,"humaneval.jsonl"),"r", encoding="utf8") as f:
        for line in f.readlines():
            obj = json.loads(line)
            prompt = obj["prompt"]
            if lang == "java":
                comment_end = prompt.find("*/") + 2
                method_args_start = prompt.find("(", comment_end)
                method_family = prompt[comment_end:method_args_start]
                obj["entry_point"] = method_family.split()[-1]
                print("+"*50)
                print(obj["entry_point"])
                print("-" * 50)
                print(prompt)
                print("+" * 50)
                lines.append(obj)

    with jsonlines.open(os.path.join(dataset_dir,"HumanEval_{lang}.jsonl".format(lang=lang)), mode='w') as writer:
        for line in lines:
            jsonlines.Writer.write(writer, line)

# add_entry_points(python_dir, "py")
add_entry_points(java_dir, "java")
# add_entry_points(cpp_dir, "cpp")
# add_entry_points(js_dir, "js")
# add_entry_points(go_dir, "go")

# import pdb; pdb.set_trace()
