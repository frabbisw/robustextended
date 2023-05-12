#!/bin/bash -l
#$ -N js_func_name_FuncRenameInflectionalVariation
#$ -cwd
#$ -l m_mem_free=50G
#$ -l g=1
#$ -j y
# set modules
module load anaconda/3.2019.10/default
module load cuda/11.4/default
module load python/3.7.3/default
# activate conda env
cd /home/f_rabbi/recode/recode_multi/run_code
source activate ReCode
export LD_LIBRARY_PATH=/home/f_rabbi/.conda/envs/ReCode/lib/python3.8/site-packages/nvidia/cublas/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/f_rabbi/.conda/envs/conda_env/lib:$LD_LIBRARY_PATH
# run job
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s3.jsonl ../datasets/codegen6bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s1.jsonl ../datasets/codegen6bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s0.jsonl ../datasets/codegen6bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s4.jsonl ../datasets/codegen6bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s2.jsonl ../datasets/codegen6bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
