#!/bin/bash
#SBATCH -J js_incoder1b_new # job name
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_nominal_f_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nominal/ incoder1b
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_partial_f_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/partial/ incoder1b

python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameButterFinger incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameChangeChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameChangeChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameChangeChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSnakeCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSwapChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameChangeChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameButterFinger incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameChangeChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameButterFinger incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSwapChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSnakeCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSwapChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSwapChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSnakeCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSnakeCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSynonymSub incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSynonymSub incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSynonymSub incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSynonymSub incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSwapChar incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameButterFinger incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameButterFinger incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSynonymSub incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/func_name/FuncRenameSnakeCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/BackTranslation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/BackTranslation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymInsertion incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ChangeCharCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ChangeCharCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/BackTranslation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/BackTranslation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymInsertion incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ChangeCharCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ChangeCharCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymInsertion incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/ChangeCharCase incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymInsertion incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s4.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s2.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/BackTranslation incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s3.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SynonymInsertion incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s0.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture incoder1b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s1.jsonl ../datasets/incoder1b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation incoder1b

module unload cuda/12.0.0
module unload python/3.9.6
module unload anaconda/3.2023.03
