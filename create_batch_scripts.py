import os

lang = "js"
dataset_dir = f"datasets/perturbed/humaneval{lang}/full"
generated_dir = "datasets/codegen6bmulti/generated_pass5_1"
with open("run_code/bash_template.sh", "r") as f:
    template = f.read()

task_dict = {}

for method_name in os.listdir(dataset_dir):
    # print(method_name)
    method_dir = os.path.join(dataset_dir, method_name)
    for file_name in os.listdir(method_dir):
        file_path = os.path.join("..", os.path.join(method_dir, file_name))
        # print(file_path, os.path.isfile(file_path))
        new_folder_name = file_name[file_name.find("_")+1:file_name.rfind("_")]
        output_path = os.path.join("..", os.path.join(os.path.join(os.path.join(os.path.join(generated_dir, lang), method_name), new_folder_name)))
        generate_command = f"python generate_single_code_single_gpu.py {file_path} {output_path}"
        # print(generate_command)
        task_name = f"{lang}_{method_name}_{new_folder_name}"
        if task_name not in task_dict.keys():
            task_dict[task_name] = ""
        task_dict[task_name] += (generate_command + "\n")
        # sh_file_contents = template.replace("{command}",generate_command).replace("{task_name}",task_name)
        # print(sh_file_contents)
        # with open(f"batch_files/{task_name}.sh", "w") as f:
        #     print(f"qsub {task_name}.sh")
        #     f.write(sh_file_contents)

        # print(task_name)
        ####change dir while evaluating java code####tmp is the current dir###
        # print(file_path)

for task_name in task_dict.keys():
    sh_file_contents = template.replace("{command}", task_dict[task_name]).replace("{task_name}", task_name)
    with open(f"batch_files/{task_name}.sh", "w") as f:
        print(f"qsub {task_name}.sh")
        f.write(sh_file_contents)
