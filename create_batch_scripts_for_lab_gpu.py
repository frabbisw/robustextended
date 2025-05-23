import os

lang = "cpp"
model_name = "codegen2bmulti"
gpu_number = 0

dataset_dir = f"datasets/perturbed/humaneval{lang}/full"
generated_dir = f"datasets/{model_name}/generated_pass5_1"

task_dict = {}

for method_name in os.listdir(dataset_dir):
    # print(method_name)
    method_dir = os.path.join(dataset_dir, method_name)
    for file_name in os.listdir(method_dir):
        file_path = os.path.join("..", os.path.join(method_dir, file_name))
        # print(file_path, os.path.isfile(file_path))
        new_folder_name = file_name[file_name.find("_")+1:file_name.rfind("_")]
        output_path = os.path.join("..", os.path.join(os.path.join(os.path.join(os.path.join(generated_dir, lang), method_name), new_folder_name)))
        generate_command = f"python ../run_code/generate_code_from_lab_gpu_all.py {file_path} {output_path} {model_name} {gpu_number}"

        task_name = f"{lang}_{method_name}_{new_folder_name}"
        if task_name not in task_dict.keys():
            task_dict[task_name] = ""
        task_dict[task_name] += (generate_command + "\n")

all_batches = ""
for task_name in task_dict.keys():
    all_batches += f"./{task_name}.sh\n"
    with open(f"batch_files_lab_gpu{gpu_number+1}/{task_name}.sh", "w") as f:
        f.write(task_dict[task_name])

with open(f"batch_files_lab_gpu{gpu_number+1}/all_batches.sh", "w") as f:
    f.write(all_batches)