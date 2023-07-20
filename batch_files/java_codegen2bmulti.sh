#!/bin/bash -l
#$ -N java_codegen2bmulti
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
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/nominal/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/partial/f_s0.jsonl codegen2bmulti

python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/split_lines/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/split_lines/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/split_lines/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/split_lines/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/split_lines/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_afterdoc/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_afterdoc/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_afterdoc/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_afterdoc/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_afterdoc/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_aftercode/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_aftercode/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_aftercode/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_aftercode/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_line_aftercode/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/tab_indent/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/tab_indent/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/tab_indent/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/tab_indent/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/tab_indent/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/doc2comments/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/doc2comments/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/doc2comments/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/doc2comments/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/doc2comments/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_lines/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_lines/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_lines/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_lines/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/format/new_lines/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/OperandSwap/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/OperandSwap/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/OperandSwap/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/OperandSwap/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/OperandSwap/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/ForWhileTransformer/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/ForWhileTransformer/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/ForWhileTransformer/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/ForWhileTransformer/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/ForWhileTransformer/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerNaive/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerNaive/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerNaive/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerNaive/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerNaive/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/DeadCodeInserter/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerRN/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerRN/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerRN/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerRN/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerRN/f_s0.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerCB/f_s2.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerCB/f_s3.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerCB/f_s4.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerCB/f_s1.jsonl codegen2bmulti
python generate_codes_only_for_changed_prompts.py ../datasets/codegen2bmulti/generated_pass5_1/java/natgen/VarRenamerCB/f_s0.jsonl codegen2bmulti

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
