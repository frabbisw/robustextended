import os
langs = ["java","cpp","js"]
model_names = ["codegen2bmulti", "codegen6bmulti", "incoder1b", "incoder6b"]
for model_name in model_names:
    for lang in langs:
        print(lang)
        task_name = f"{lang}_{model_name}"
        dataset_dir = f"datasets/{model_name}/generated_pass5_1/{lang}"
        with open("run_code/bash_template.sh", "r") as f:
            template = f.read()

        task_command = ""
        task_command = task_command + f"python generate_codes_only_for_changed_prompts.py ../datasets/{model_name}/generated_pass5_1/{lang}/nominal/f_s0.jsonl {model_name}\n"
        task_command = task_command + f"python generate_codes_only_for_changed_prompts.py ../datasets/{model_name}/generated_pass5_1/{lang}/partial/f_s0.jsonl {model_name}\n\n"

        for method_name in os.listdir(dataset_dir):
            if method_name not in ["natgen","format"]:
                continue
            method_dir = os.path.join(dataset_dir, method_name)
            for aug_method in os.listdir(method_dir):
                aug_method_dir = os.path.join(method_dir, aug_method)
                if os.path.isfile(aug_method_dir):
                    continue
                for file_name in os.listdir(aug_method_dir):
                    file_path = os.path.join("..", os.path.join(aug_method_dir, file_name))
                    generate_command = f"python generate_codes_only_for_changed_prompts.py {file_path} {model_name}\n"
                    task_command += generate_command
                    print(generate_command)


        sh_file_contents = template.replace("{command}", task_command)
        sh_file_contents = sh_file_contents.replace("{task_name}", task_name)
        with open(f"batch_files/{task_name}.sh", "w") as f:
            print(f"qsub {task_name}.sh")
            f.write(sh_file_contents)