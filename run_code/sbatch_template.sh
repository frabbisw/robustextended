#!/bin/bash

#SBATCH -J {task_name}
#SBATCH -n4
#SBATCH --mem=10GB
#SBATCH --gpus=1
#SBATCH --time=<TIME>
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

cd ../run_code

{command}
