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
            elif lang == "cpp":
                comment_end = prompt.find("*/") + 2
                method_args_start = prompt.find("(", comment_end)
                garbage = prompt[comment_end:method_args_start]
                try:
                    obj["entry_point"] = garbage.split()[-1]
                    print(obj["entry_point"])
                    lines.append(obj)
                except:
                    method_args_end = prompt[:prompt.rfind("/*")].rfind("(")
                    obj["entry_point"] = prompt[:method_args_end].split()[-1]
                    print(obj["entry_point"])
                    lines.append(obj)
            elif lang == "go":
                try:
                    last_first_bracket_index = prompt.rfind("(")
                    parts = prompt[:last_first_bracket_index].split()
                    obj["entry_point"] = parts[-1]
                    print(obj["entry_point"])
                    lines.append(obj)
                except:
                    print(prompt)
            elif lang == "js":
                comment_end = prompt.find("*/") + 2
                method_args_start = prompt.find("=", comment_end)
                garbage = prompt[comment_end:method_args_start]
                try:
                    obj["entry_point"] = garbage.split()[-1]
                    print(obj["entry_point"])
                    lines.append(obj)
                except:
                    print(prompt)
            else:
                print("*"*50)
                print(prompt)

    with jsonlines.open(os.path.join(dataset_dir,"HumanEval_{lang}.jsonl".format(lang=lang)), mode='w') as writer:
        for line in lines:
            jsonlines.Writer.write(writer, line)

lang = "go"

# add_entry_points(python_dir, "py")
# add_entry_points(java_dir, "java")
add_entry_points(f"datasets/nominal/humaneval-x/data/{lang}/data", lang)
# add_entry_points(js_dir, "js")
# add_entry_points(go_dir, "go")

# import pdb; pdb.set_trace()