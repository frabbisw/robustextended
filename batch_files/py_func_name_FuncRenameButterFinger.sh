#!/bin/bash -l
#$ -N py_func_name_FuncRenameButterFinger
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
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalpy/full/func_name/humanevalpy_FuncRenameButterFinger_s0.jsonl ../datasets/codegen6bmulti/generated_pass5_1/py/func_name/FuncRenameButterFinger codegen6bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalpy/full/func_name/humanevalpy_FuncRenameButterFinger_s1.jsonl ../datasets/codegen6bmulti/generated_pass5_1/py/func_name/FuncRenameButterFinger codegen6bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalpy/full/func_name/humanevalpy_FuncRenameButterFinger_s2.jsonl ../datasets/codegen6bmulti/generated_pass5_1/py/func_name/FuncRenameButterFinger codegen6bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalpy/full/func_name/humanevalpy_FuncRenameButterFinger_s3.jsonl ../datasets/codegen6bmulti/generated_pass5_1/py/func_name/FuncRenameButterFinger codegen6bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalpy/full/func_name/humanevalpy_FuncRenameButterFinger_s4.jsonl ../datasets/codegen6bmulti/generated_pass5_1/py/func_name/FuncRenameButterFinger codegen6bmulti

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
