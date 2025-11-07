import os

def round_to_nearest_quarter(num):
    try:
        num = float(num)
        allowed_values = [0, 0.25, 0.5, 0.75, 1]
        nearest = min(allowed_values, key=lambda x: abs(x - num))
        return nearest
    except:
        return .75

def tune(filename):
    updated_groups = []
    with open(filename, "r") as f:
        contents = f.read()
    groups = contents.split("\n\n")
    for group in groups:
        group = group.strip()
        print(group)
        print("---")
        unique_id, pert, nom, sem = group.split("\n")
        unique_id = unique_id.split(" ")[0].strip()
                
        pert = round_to_nearest_quarter(pert.split(":")[-1].strip())
        nom = round_to_nearest_quarter(nom.split(":")[-1].strip())
        sem = round_to_nearest_quarter(sem.split(":")[-1].strip())
        # print(pert, nom, sem)
        updated_groups.append(f"{unique_id}\nPerturbed prompt:{pert}\nNominal prompt:{nom}\nSemantic:{sem}")

    with open(f"{filename.replace('.txt', '_n.txt')}", "w") as f:
        f.write("\n\n".join(updated_groups))

import sys
tune(sys.argv[1])
