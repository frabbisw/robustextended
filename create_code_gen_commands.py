import os

lang = "java"
dataset_dir = f"datasets/perturbed/humaneval{lang}/full"
generated_dir = "datasets/generated"

for method_name in os.listdir(dataset_dir):
    # print(method_name)
    method_dir = os.path.join(dataset_dir, method_name)
    for file_name in os.listdir(method_dir):
        file_path = os.path.join("..", os.path.join(method_dir, file_name))
        # print(file_path, os.path.isfile(file_path))
        new_folder_name = file_name[file_name.find("_")+1:file_name.rfind("_")]
        output_path = os.path.join("..", os.path.join(os.path.join(os.path.join(os.path.join(generated_dir, lang), method_name), new_folder_name)))
        generate_command = f"python generate_code_without_batch_files.py {file_path} {output_path}"
        print(generate_command)
        ####change dir while evaluating java code####tmp is the current dir###
        # print(file_path)