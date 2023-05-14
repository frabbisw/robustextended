#!/bin/bash -l
#$ -N js_format_doc2comments
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevalcpp_nominal_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/cpp/nominal/ codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/nominal/humanevalcpp_partial_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/cpp/partial/ codegen2bmulti

python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljava_nominal_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/java/nominal/ codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljava_partial_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/java/partial/ codegen2bmulti

python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_nominal_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nominal/ codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_partial_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/partial/ codegen2bmulti

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
