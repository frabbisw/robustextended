template = '''
#!/bin/bash

#SBATCH -J ##batch_name##
#SBATCH -n4
#SBATCH --mem=10GB
#SBATCH --gpus=1
#SBATCH --time=##TIME##
#SBATCH -o _%x%J.out
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=osdefr@gmail.com

source /etc/profile.d/modules.sh

module load java/17.0.2
module load gcc/11.5
module load go/1.24.5
module load python/3.11.6
module load cuda/12.3.2
module load anaconda/3.2024.10.1

eval "$(conda shell.bash hook)"

conda activate code_trans

###COMMANDS###
'''

import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys

def prep_block(file_path, lang, part):
    return = f'''
    python parse_nl.py {file_path} {lang}
    python pre_docstring.py {file_path} magicoder7b
    python post_docstring.py {file_path} 
    python generate_code.py {file_path} magicoder7b
    python test_single.py {file_path} {lang} {int(part)}
    '''


part_dict = {"1": ["BackTranslation", "SynonymInsertion"], "2": ["ButterFingersPerturbation", "SynonymSubstitution"], "3": ["ChangeCharCase", "TenseTransformationFuture"], "4": ["EnglishInflectionalVariation", "TenseTransformationPast"], "5": "SwapCharactersPerturbation, WhitespacePerturbation"}

lang = sys.argv[1]
part = sys.argv[2]
tm = sys.argv[3]

folder_path = f"/home/f_rabbi/recode/robustextended/datasets/magicoder7b/generated_pass5_1/{lang}/nlaugmenter/"

all_blocks = ""
for pert in part_dict[part]:
    pert_path = os.path.join(folder_path, pert)
    for i in range(5):
        file_path = os.path.join(pert_path, f"f_s{str(i)}.jsonl")
        block = prep_block(file_path, lang, part)
        all_blocks += (block + "\n")

template = template.replace("##TIME##", tm).replace("##batch_name##", f"allpre_{lang}_{part}").replace("###COMMANDS###", all_blocks)

with open(f"allpre_{lang}_{part}.sh", "w") as f:
    f.write(template)

