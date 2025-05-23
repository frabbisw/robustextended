import json
import os
import jsonlines

dataset_dir = "datasets/nominal"
python_dir = "datasets/nominal/humaneval-x/data/python/data"
java_dir = "datasets/nominal/humaneval-x/data/java/data"
cpp_dir = "datasets/nominal/humaneval-x/data/cpp/data"
go_dir = "datasets/nominal/humaneval-x/data/go/data"
js_dir = "datasets/nominal/humaneval-x/data/js/data"
human_eval_with_entry_point_path = "datasets/nominal/HumanEval.jsonl"

def python_to_others(entry_point):
    if entry_point == "": return ""
    if "_" in entry_point:
        # has_close_elements => hasCloseElements
        new_func_name = str(entry_point)
        words = new_func_name.split("_")
        new_words = [words[0]]
        for word in words[1:]:
            chars = list(word)
            if len(chars) == 0: continue
            chars[0] = chars[0].upper()
            new_words.append("".join(chars))
        new_func_name = "".join(new_words)
    else:
        # hasCloseElements => has_close_elements
        new_func_name = entry_point[0]
        for ch in entry_point[1:]:
            if ch.isupper():
                new_func_name += "_" + ch.lower()
            else:
                new_func_name += ch
    return new_func_name

def python_to_go(entry_point):
    if entry_point == "": return ""
    new_func_name = python_to_others(entry_point)
    new_func_name = new_func_name[0].upper() + new_func_name[1:]
    return new_func_name

def add_entry_points(dir, entry_points, lang):
    lines = []
    cnt = 0
    with open(os.path.join(dir,"humaneval.jsonl"),"r", encoding="utf8") as f:
        for line in f.readlines():
            obj = json.loads(line)
            old_entry_point = entry_points[cnt]
            if lang == "go":
                new_entry_point = python_to_go(entry_points[cnt])
            elif lang == "py":
                new_entry_point = entry_points[cnt]
            else:
                new_entry_point = python_to_others(entry_points[cnt])
            obj["entry_point"] = new_entry_point
            obj["prompt"] = obj["prompt"].replace(old_entry_point, new_entry_point)
            lines.append(obj)
            cnt += 1

    with jsonlines.open(os.path.join(dataset_dir,"HumanEval_{lang}.jsonl".format(lang=lang)), mode='w') as writer:
        for line in lines:
            jsonlines.Writer.write(writer, line)

def load_entry_points(path):
    entry_points = []
    with open(path,"r") as f:
        for line in f.readlines():
            obj = json.loads(line)
            entry_points.append(obj["entry_point"])
    return entry_points

entry_points = load_entry_points(human_eval_with_entry_point_path)

add_entry_points(python_dir, entry_points, "py")
add_entry_points(java_dir, entry_points, "java")
add_entry_points(cpp_dir, entry_points, "cpp")
add_entry_points(js_dir, entry_points, "js")
add_entry_points(go_dir, entry_points, "go")

# import pdb; pdb.set_trace()
