#!/bin/bash

#SBATCH -J js_mag_gen
#SBATCH -n4
#SBATCH --mem=10GB
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH -o _%x%J.out
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=osdefr@gmail.com

source /etc/profile.d/modules.sh

module load js/17.0.2
module load gcc/11.5
module load go/1.24.5
module load python/3.11.6
module load cuda/12.3.2
module load anaconda/3.2024.10.1
export PATH="$HOME/my-nodejs/bin:$PATH"
source ~/.bashrc

eval "$(conda shell.bash hook)"

conda activate code_trans

rm -r ../datasets/samples/magicoder7b/js/
python sampling.py magicoder7b js nlaugmenter
python preprocess_docstring.py /home/f_rabbi/recode/robustextended/datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl magicoder7b
python postprocess_docstring.py magicoder7b js nlaugmenter > process_logs_js.txt
python generate_code.py /home/f_rabbi/recode/robustextended/datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl magicoder7b
python prepare_orgs.py ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nominal/f_s0.jsonl ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368_org.jsonl
echo "original correct items"
python test_single_old.py ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368_org.jsonl js ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368_org.jsonl 2
echo "perturbed correct items"
python test_single_old.py ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl js ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl 3
echo "processed correct items"
python test_single.py ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368.jsonl js ../datasets/samples/magicoder7b/js/nlaugmenter/sample_368_r.jsonl 3
echo "Done!"
