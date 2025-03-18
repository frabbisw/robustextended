#!/bin/bash
#SBATCH -J {task_name} # job name
#SBATCH --account=f_rabbi # indicates username (mandatory parameter)
#SBATCH --mem=10G # memory reserved (mandatory parameter)
#SBATCH -o _%x%J.out # output (& error) file name
source /etc/profile.d/modules.sh # adding module binaries
module load cuda/12.0.0
module load python/3.9.6
module load anaconda/3.2023.03
conda init
source /home/f_rabbi/.bashrc
conda activate ReCode
{command}
module unload cuda/12.0.0
module unload python/3.9.6
module unload anaconda/3.2023.03
