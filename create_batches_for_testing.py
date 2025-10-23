import os
import sys

if len(sys.argv) < 5:
    exit(1)

TL = sys.argv[1]
model_name = sys.argv[2]
lang = sys.argv[3]
testing_folder_number = sys.argv[4]
test_case = sys.argv[5]
if test_case not in ["he", "ep"]:
    test_case = "ep"

task_name = f"{lang}_{model_name}"
task_command = f"python calculate_pass_status.py {model_name} {lang} {testing_folder_number} {task_name} {test_case}"

with open("evalplus/sbatch_template.sh", "r") as f:
  template = f.read()

sh_file_contents = template.replace("{command}", task_command)
sh_file_contents = sh_file_contents.replace("{task_name}", task_name)
sh_file_contents = sh_file_contents.replace("<TIME>", TL)
with open(f"batch_files/{task_name}.sh", "w") as f:
    print(f"qsub {task_name}.sh")
    f.write(sh_file_contents)
