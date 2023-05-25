#!/bin/bash -l
#$ -N cpp_codegen6b
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevalcpp_nominal_f_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nominal/ codegen6b
python generate_single_code_single_gpu.py ../datasets/nominal/humanevalcpp_partial_f_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/partial/ codegen6b

python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameChangeChar_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameChangeChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameButterFinger_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameButterFinger codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSynonymSub_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSynonymSub codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSwapChar_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSwapChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameInflectionalVariation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSynonymSub_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSynonymSub codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSnakeCase_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSnakeCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameButterFinger_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameButterFinger codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameButterFinger_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameButterFinger codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSnakeCase_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSnakeCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSwapChar_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSwapChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSwapChar_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSwapChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSnakeCase_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSnakeCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameButterFinger_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameButterFinger codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameButterFinger_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameButterFinger codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameCamelCase_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameCamelCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameInflectionalVariation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSynonymSub_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSynonymSub codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameChangeChar_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameChangeChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameCamelCase_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameCamelCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSwapChar_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSwapChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameChangeChar_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameChangeChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSnakeCase_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSnakeCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameInflectionalVariation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameCamelCase_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameCamelCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSnakeCase_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSnakeCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameChangeChar_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameChangeChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameInflectionalVariation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSwapChar_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSwapChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSynonymSub_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSynonymSub codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameCamelCase_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameCamelCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameInflectionalVariation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameCamelCase_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameCamelCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameChangeChar_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameChangeChar codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/func_name/humanevalcpp_FuncRenameSynonymSub_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/func_name/FuncRenameSynonymSub codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_split_lines_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/split_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_tab_indent_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/tab_indent codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_doc2comments_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/doc2comments codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_aftercode codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_tab_indent_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/tab_indent codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_aftercode codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_split_lines_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/split_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_afterdoc_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_afterdoc codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_lines_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_doc2comments_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/doc2comments codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_afterdoc_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_afterdoc codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_afterdoc_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_afterdoc codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_split_lines_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/split_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_split_lines_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/split_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_afterdoc_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_afterdoc codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_tab_indent_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/tab_indent codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_aftercode codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_split_lines_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/split_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_afterdoc_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_afterdoc codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_lines_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_lines_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_lines_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_lines_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_lines codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_doc2comments_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/doc2comments codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_doc2comments_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/doc2comments codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_doc2comments_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/doc2comments codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_aftercode codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_tab_indent_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/tab_indent codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/new_line_aftercode codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/format/humanevalcpp_tab_indent_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/format/tab_indent codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymSubstitution_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymSubstitution codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymInsertion_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymInsertion codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymInsertion_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymInsertion codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ButterFingersPerturbation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ButterFingersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationPast_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationPast codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_WhitespacePerturbation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/WhitespacePerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SwapCharactersPerturbation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SwapCharactersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymSubstitution_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymSubstitution codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationPast_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationPast codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationFuture_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationFuture codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SwapCharactersPerturbation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SwapCharactersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationFuture_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationFuture codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_BackTranslation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/BackTranslation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ButterFingersPerturbation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ButterFingersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ChangeCharCase_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ChangeCharCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_BackTranslation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/BackTranslation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymInsertion_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymInsertion codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymSubstitution_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymSubstitution codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymSubstitution_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymSubstitution codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ButterFingersPerturbation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ButterFingersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_BackTranslation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/BackTranslation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_EnglishInflectionalVariation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/EnglishInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_EnglishInflectionalVariation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/EnglishInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ChangeCharCase_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ChangeCharCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ButterFingersPerturbation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ButterFingersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationFuture_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationFuture codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymInsertion_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymInsertion codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_BackTranslation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/BackTranslation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationPast_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationPast codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationPast_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationPast codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationPast_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationPast codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ChangeCharCase_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ChangeCharCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationFuture_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationFuture codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_TenseTransformationFuture_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/TenseTransformationFuture codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_WhitespacePerturbation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/WhitespacePerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SwapCharactersPerturbation_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SwapCharactersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_WhitespacePerturbation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/WhitespacePerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_EnglishInflectionalVariation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/EnglishInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_BackTranslation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/BackTranslation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SwapCharactersPerturbation_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SwapCharactersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SwapCharactersPerturbation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SwapCharactersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ChangeCharCase_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ChangeCharCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_WhitespacePerturbation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/WhitespacePerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ButterFingersPerturbation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ButterFingersPerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_EnglishInflectionalVariation_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/EnglishInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_EnglishInflectionalVariation_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/EnglishInflectionalVariation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymInsertion_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymInsertion codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_SynonymSubstitution_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/SynonymSubstitution codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_WhitespacePerturbation_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/WhitespacePerturbation codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/nlaugmenter/humanevalcpp_ChangeCharCase_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/nlaugmenter/ChangeCharCase codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerNaive_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerNaive codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerRN_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerRN codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_OperandSwap_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/OperandSwap codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_DeadCodeInserter_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/DeadCodeInserter codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_OperandSwap_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/OperandSwap codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerNaive_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerNaive codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_OperandSwap_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/OperandSwap codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerCB_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerCB codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_ForWhileTransformer_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/ForWhileTransformer codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_ForWhileTransformer_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/ForWhileTransformer codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_DeadCodeInserter_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/DeadCodeInserter codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerRN_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerRN codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_DeadCodeInserter_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/DeadCodeInserter codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerRN_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerRN codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_OperandSwap_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/OperandSwap codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerCB_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerCB codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerNaive_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerNaive codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_ForWhileTransformer_s0.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/ForWhileTransformer codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerCB_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerCB codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerRN_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerRN codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_ForWhileTransformer_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/ForWhileTransformer codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_ForWhileTransformer_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/ForWhileTransformer codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerCB_s2.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerCB codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerNaive_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerNaive codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_DeadCodeInserter_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/DeadCodeInserter codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_DeadCodeInserter_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/DeadCodeInserter codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerNaive_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerNaive codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_OperandSwap_s4.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/OperandSwap codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerCB_s3.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerCB codegen6b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevalcpp/full/natgen/humanevalcpp_VarRenamerRN_s1.jsonl ../datasets/codegen6b/generated_pass5_1/cpp/natgen/VarRenamerRN codegen6b

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
