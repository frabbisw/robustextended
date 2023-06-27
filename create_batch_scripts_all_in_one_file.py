import os
langs = ["java","cpp","js"]
model_name = "codegen2bmulti"

for lang in langs:
    task_name = f"{lang}_{model_name}"
    dataset_dir = f"datasets/perturbed/humaneval{lang}/full"
    generated_dir = f"datasets/{model_name}/generated_pass5_1"
    with open("run_code/bash_template.sh", "r") as f:
        template = f.read()

    task_command = ""
    task_command = task_command + f"python generate_single_code_single_gpu.py ../datasets/nominal/humaneval{lang}_nominal_f_s0.jsonl ../datasets/{model_name}/generated_pass5_1/{lang}/nominal/ {model_name}\n"
    task_command = task_command + f"python generate_single_code_single_gpu.py ../datasets/nominal/humaneval{lang}_partial_f_s0.jsonl ../datasets/{model_name}/generated_pass5_1/{lang}/partial/ {model_name}\n\n"

    for method_name in os.listdir(dataset_dir):
        # print(method_name)
        method_dir = os.path.join(dataset_dir, method_name)
        for file_name in os.listdir(method_dir):
            file_path = os.path.join("..", os.path.join(method_dir, file_name))
            # print(file_path, os.path.isfile(file_path))
            new_folder_name = file_name[file_name.find("_")+1:file_name.rfind("_")]
            output_path = os.path.join("..", os.path.join(os.path.join(os.path.join(os.path.join(generated_dir, lang), method_name), new_folder_name)))
            generate_command = f"python generate_single_code_single_gpu.py {file_path} {output_path} {model_name}\n"
            task_command += generate_command
            print(generate_command)


    sh_file_contents = template.replace("{command}", task_command)
    sh_file_contents = sh_file_contents.replace("{task_name}", task_name)
    with open(f"batch_files/{task_name}.sh", "w") as f:
        print(f"qsub {task_name}.sh")
        f.write(sh_file_contents)