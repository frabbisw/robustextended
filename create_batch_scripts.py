import os

dataset_dir = "datasets/perturbed/humanevaljava/full"
generated_dir = "datasets/generated"
lang = "java"
with open("run_code/bash_template.sh", "r") as f:
    template = f.read()

for method_name in os.listdir(dataset_dir):
    # print(method_name)
    method_dir = os.path.join(dataset_dir, method_name)
    for file_name in os.listdir(method_dir):
        file_path = os.path.join("..", os.path.join(method_dir, file_name))
        # print(file_path, os.path.isfile(file_path))
        new_folder_name = file_name[file_name.find("_")+1:file_name.rfind("_")]
        output_path = os.path.join("..", os.path.join(os.path.join(os.path.join(os.path.join(generated_dir, lang), method_name), new_folder_name)))
        generate_command = f"python generate_code.py {file_path} {output_path}"
        # print(generate_command)
        task_name = f"{lang}_{method_name}_{new_folder_name}"
        sh_file_contents = template.replace("{command}",generate_command).replace("{task_name}",task_name)
        # print(sh_file_contents)
        with open(f"batch_files/{task_name}.sh", "w") as f:
            f.write(sh_file_contents)

        # print(generate_command)
        ####change dir while evaluating java code####tmp is the current dir###
        # print(file_path)