#!/bin/bash -l
#$ -N js_codegen2bmulti_new
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_nominal_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nominal/ codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_partial_f_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/partial/ codegen2bmulti

python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameButterFinger codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameChangeChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameChangeChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameChangeChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSnakeCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSwapChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameChangeChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameButterFinger codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameChangeChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameButterFinger codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSwapChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSnakeCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSwapChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSwapChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSnakeCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSnakeCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSynonymSub codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSynonymSub codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSynonymSub codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSynonymSub codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSwapChar codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameButterFinger codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameButterFinger codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSynonymSub codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/func_name/FuncRenameSnakeCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/BackTranslation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/BackTranslation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymSubstitution codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymSubstitution codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymInsertion codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ChangeCharCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ChangeCharCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymSubstitution codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/BackTranslation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationPast codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationPast codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/BackTranslation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymInsertion codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ChangeCharCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ChangeCharCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymInsertion codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/ChangeCharCase codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymSubstitution codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationPast codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationPast codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationPast codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymSubstitution codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymInsertion codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s4.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s2.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/BackTranslation codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s3.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SynonymInsertion codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s0.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture codegen2bmulti
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s1.jsonl ../datasets/codegen2bmulti/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation codegen2bmulti

# clean loaded modules
module unload anaconda/3.2019.10/default
module unload cuda/11.4/default
module unload python/3.7.3/default
