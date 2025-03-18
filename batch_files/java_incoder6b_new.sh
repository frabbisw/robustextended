#!/bin/bash
#SBATCH -J java_incoder6b_new # job name
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
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljava_nominal_f_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/nominal/ incoder6b
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljava_partial_f_s0.jsonl ../datasets/incoder6b/generated_pass5_1/java/partial/ incoder6b

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

module unload cuda/12.0.0
module unload python/3.9.6
module unload anaconda/3.2023.03
