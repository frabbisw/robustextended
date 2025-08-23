#!/bin/bash

#SBATCH -J js_magicoder7b_new
#SBATCH -n4
#SBATCH --mem=10GB
#SBATCH --gpus=1
#SBATCH --time=<TIME>
#SBATCH -o _%x%J.out
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=osdefr@gmail.com

source /etc/profile.d/modules.sh

module load java/17.0.2
module load gcc/11.5
module load go/1.24.5
module load python/3.11.6
module load cuda/12.3.2
module load anaconda/3.2024.10.1

eval "$(conda shell.bash hook)"

conda activate ReCode

cd ../run_code

python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_nominal_f_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nominal/ magicoder7b
python generate_single_code_single_gpu.py ../datasets/nominal/humanevaljs_partial_f_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/partial/ magicoder7b

python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSnakeCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameChangeChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSnakeCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSynonymSub magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameChangeChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSnakeCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameChangeChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSnakeCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameButterFinger magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameChangeChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSwapChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSynonymSub magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameButterFinger magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSwapChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameChangeChar_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameChangeChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameButterFinger magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSynonymSub magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSwapChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSynonymSub magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameButterFinger magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSnakeCase_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSnakeCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSwapChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameButterFinger_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameButterFinger magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSynonymSub_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSynonymSub magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameInflectionalVariation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/func_name/humanevaljs_FuncRenameSwapChar_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/func_name/FuncRenameSwapChar magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ChangeCharCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/BackTranslation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymInsertion magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/BackTranslation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ChangeCharCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymInsertion magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SwapCharactersPerturbation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SwapCharactersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/BackTranslation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ChangeCharCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymSubstitution_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymSubstitution magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ButterFingersPerturbation_s4.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ButterFingersPerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymInsertion magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ChangeCharCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/BackTranslation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s2.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymInsertion magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_ChangeCharCase_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/ChangeCharCase magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_BackTranslation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/BackTranslation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationFuture_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationFuture magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_SynonymInsertion_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/SynonymInsertion magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_WhitespacePerturbation_s3.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/WhitespacePerturbation magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_TenseTransformationPast_s1.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/TenseTransformationPast magicoder7b
python generate_single_code_single_gpu.py ../datasets/perturbed/humanevaljs/full/nlaugmenter/humanevaljs_EnglishInflectionalVariation_s0.jsonl ../datasets/magicoder7b/generated_pass5_1/js/nlaugmenter/EnglishInflectionalVariation magicoder7b

