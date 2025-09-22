import json
import sys
import jsonlines

pert_filepath = sys.argv[1]
nom_filepath = sys.argv[2]
new_filepath = sys.argv[3]

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts
def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

pert_prompts = load_prompts(pert_filepath)
nom_prompts = load_prompts(nom_filepath)


nom_dict = {}
for p in nom_prompts:
    nom_dict[p["task_id"]] = p

nom_lines = []
for p in pert_prompts:
    nom_lines.append(nom_dict[p["task_id"]])

save_prompts(new_filepath, nom_lines)
print("saved", new_filepath)
