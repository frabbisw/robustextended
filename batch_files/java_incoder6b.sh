#!/bin/bash -l
#$ -N java_incoder6b
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljava_nominal_f_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nominal/ incoder6b
python generate_single_code_single_gpu.py ../datasets/partial/humanevaljava_partial_f_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/partial/ incoder6b

python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSnakeCase_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSnakeCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSnakeCase_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSnakeCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameInflectionalVariation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameButterFinger_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameButterFinger incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSynonymSub_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSynonymSub incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameButterFinger_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameButterFinger incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameButterFinger_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameButterFinger incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameChangeChar_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameChangeChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSynonymSub_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSynonymSub incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSwapChar_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSwapChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSnakeCase_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSnakeCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSwapChar_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSwapChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameInflectionalVariation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameInflectionalVariation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameChangeChar_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameChangeChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameButterFinger_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameButterFinger incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameInflectionalVariation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSwapChar_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSwapChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameChangeChar_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameChangeChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSnakeCase_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSnakeCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameInflectionalVariation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSynonymSub_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSynonymSub incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameButterFinger_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameButterFinger incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSwapChar_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSwapChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSnakeCase_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSnakeCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSynonymSub_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSynonymSub incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameChangeChar_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameChangeChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSwapChar_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSwapChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameChangeChar_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameChangeChar incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/func_name/humanevaljava_FuncRenameSynonymSub_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/func_name/FuncRenameSynonymSub incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_aftercode_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_aftercode incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_doc2comments_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/doc2comments incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_tab_indent_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/tab_indent incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_afterdoc_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_afterdoc incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_lines_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_split_lines_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/split_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_afterdoc_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_afterdoc incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_lines_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_tab_indent_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/tab_indent incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_split_lines_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/split_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_afterdoc_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_afterdoc incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_doc2comments_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/doc2comments incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_afterdoc_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_afterdoc incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_aftercode_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_aftercode incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_split_lines_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/split_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_doc2comments_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/doc2comments incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_aftercode_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_aftercode incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_tab_indent_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/tab_indent incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_lines_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_split_lines_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/split_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_afterdoc_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_afterdoc incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_doc2comments_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/doc2comments incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_tab_indent_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/tab_indent incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_aftercode_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_aftercode incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_lines_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_split_lines_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/split_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_doc2comments_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/doc2comments incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_line_aftercode_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_line_aftercode incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_new_lines_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/new_lines incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/format/humanevaljava_tab_indent_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/format/tab_indent incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationPast_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationPast incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ChangeCharCase_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ChangeCharCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationPast_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationPast incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymInsertion incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_BackTranslation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/BackTranslation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymSubstitution_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymSubstitution incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_WhitespacePerturbation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/WhitespacePerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_WhitespacePerturbation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/WhitespacePerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ChangeCharCase_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ChangeCharCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ButterFingersPerturbation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ButterFingersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymSubstitution_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymSubstitution incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_EnglishInflectionalVariation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/EnglishInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_WhitespacePerturbation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/WhitespacePerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_WhitespacePerturbation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/WhitespacePerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ChangeCharCase_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ChangeCharCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationFuture_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationFuture incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ButterFingersPerturbation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ButterFingersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ButterFingersPerturbation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ButterFingersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationPast_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationPast incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SwapCharactersPerturbation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SwapCharactersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ButterFingersPerturbation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ButterFingersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationFuture_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationFuture incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SwapCharactersPerturbation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SwapCharactersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationPast_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationPast incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_EnglishInflectionalVariation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/EnglishInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationFuture_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationFuture incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationFuture_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationFuture incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymSubstitution_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymSubstitution incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_BackTranslation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/BackTranslation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymSubstitution_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymSubstitution incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SwapCharactersPerturbation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SwapCharactersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SwapCharactersPerturbation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SwapCharactersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_WhitespacePerturbation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/WhitespacePerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_BackTranslation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/BackTranslation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymInsertion incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_EnglishInflectionalVariation_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/EnglishInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationPast_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationPast incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_EnglishInflectionalVariation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/EnglishInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymInsertion incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SwapCharactersPerturbation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SwapCharactersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_EnglishInflectionalVariation_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/EnglishInflectionalVariation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymSubstitution_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymSubstitution incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ChangeCharCase_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ChangeCharCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_BackTranslation_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/BackTranslation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_TenseTransformationFuture_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/TenseTransformationFuture incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymInsertion incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_SynonymInsertion_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/SynonymInsertion incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ChangeCharCase_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ChangeCharCase incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_ButterFingersPerturbation_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/ButterFingersPerturbation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/nlaugmenter/humanevaljava_BackTranslation_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/nlaugmenter/BackTranslation incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_ForWhileTransformer_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/ForWhileTransformer incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_OperandSwap_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/OperandSwap incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_ForWhileTransformer_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/ForWhileTransformer incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerRN_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerRN incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_DeadCodeInserter_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/DeadCodeInserter incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_ForWhileTransformer_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/ForWhileTransformer incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_DeadCodeInserter_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/DeadCodeInserter incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerNaive_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerNaive incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_DeadCodeInserter_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/DeadCodeInserter incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_OperandSwap_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/OperandSwap incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerCB_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerCB incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerCB_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerCB incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_OperandSwap_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/OperandSwap incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerCB_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerCB incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_DeadCodeInserter_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/DeadCodeInserter incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_OperandSwap_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/OperandSwap incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_ForWhileTransformer_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/ForWhileTransformer incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerRN_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerRN incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerNaive_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerNaive incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_ForWhileTransformer_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/ForWhileTransformer incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerCB_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerCB incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_OperandSwap_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/OperandSwap incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerNaive_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerNaive incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerNaive_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerNaive incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_DeadCodeInserter_s3.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/DeadCodeInserter incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerCB_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerCB incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerRN_s2.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerRN incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerRN_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerRN incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerRN_s4.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerRN incoder6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljava/full/natgen/humanevaljava_VarRenamerNaive_s1.jsonl ../datasets/incoder6b/generated_pass5_1/java/natgen/VarRenamerNaive incoder6b

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
