import os

def convert(lang):
    stop_token = "="*25+"\n"+"="*25+"\n\n\n\n"
    updated_groups = []
    with open(f"{lang}_samples.txt", "r") as f:
        contents = f.read()
    groups = contents.split(stop_token)
    for group in groups:
        # task_id, _, _, _, nom, pert, sem, _  = group.split("-"*22)
        # nom = nom.split(":")[-1].strip()
        # pert = pert.split(":")[-1].strip()
        # sem = sem.split(":")[-1].strip()                
        pert = float(pert.split(":")[-1].strip())
        nom = float(nom.split(":")[-1].strip())
        sem = float(sem.split(":")[-1].strip())
        # print(pert, nom, sem)
        updated_groups.append(f"{unique_id}\nPerturbed prompt:{pert}\nNominal prompt:{nom}\nSemantic:{sem}")

    with open(f"{lang}_2.txt", "w") as f:
        f.write("\n\n".join(updated_groups))

import sys
convert(sys.argv[1])
