import json

def view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"])
    return prompts

def full_view(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line)["prompt"]+json.loads(line)["canonical_solution"])
    return prompts

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts

java_path = "../datasets/nominal/HumanEval_java.jsonl"
cpp_path = "../datasets/nominal/HumanEval_cpp.jsonl"
py_path = "../datasets/nominal/HumanEval_py.jsonl"
go_path = "../datasets/nominal/HumanEval_go.jsonl"
js_path = "../datasets/nominal/HumanEval_js.jsonl"

prompts = load_prompts(java_path)
sample_java_main = "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.List;\n" + prompts[0]["test"]
sample_java_solution = prompts[0]["prompt"] + prompts[0]["canonical_solution"]

with open("../tmp/Main.java", "w") as f:
    f.write(sample_java_main)
with open("../tmp/Solution.java", "w") as f:
    f.write(sample_java_solution)



import os
import subprocess
os.chdir("../tmp/")

try:
    # run javac command to compile Java code
    compile_output = subprocess.check_output(['javac', 'Main.java', 'Solution.java'], stderr=subprocess.STDOUT)

    # run java command to execute Main class
    run_output = subprocess.check_output(['java', 'Main'], stderr=subprocess.STDOUT)

    # print the output from the Java program
    print("the program ran successfully")
    print(run_output.decode('utf-8'))


except subprocess.CalledProcessError as e:
    # print the error message and output from the Java compiler or program
    print("An error occurred while running the program:")
    print(e.output.decode('utf-8'))
    print("Return code: ", e.returncode)

try:
    subprocess.check_output(['rm', 'Main.java', 'Solution.java', 'Main.class', 'Solution.class'])
except:
    print("can not delete files")

print("finished!!")

# import pdb; pdb.set_trace()