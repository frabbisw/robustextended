import unittest.mock
# import multiprocessing
import signal
import signal
import subprocess
from io import StringIO
from contextlib import redirect_stdout
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class TimeoutError(Exception):
    pass

def handler(signum, frame):
    if signum == signal.SIGALRM:
        raise TimeoutError("timeout")
    print('other signal')
    raise Exception("handler: unk exception")


class InputError(BaseException):
    pass


def test_a_method(code, entry_point, test_code):
    real_input = __builtins__.input
    try:
        exec(code)
    except:
        return False, "code cannot compile"
    exec(test_code, globals())
    try:
        __builtins__.input = unittest.mock.MagicMock(side_effect=InputError())
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        check(locals()[entry_point])
    except InputError as e1:
        return False, "called input()"
    except AssertionError as e2:
        return False, "cannot pass tests"
    except TimeoutError as e3:
        return False, "timeout"
    except Exception as e4:
        # print(e4)
        return False, "exception"
    finally:
        signal.alarm(0)
        __builtins__.input = real_input
    return True, "passed"




import json
import os
import jsonlines
from tqdm import tqdm as tq
import sys
import pickle
import ast
import re
from collections import Counter
def identify_argument_types(func_call_string):
    tree = ast.parse(func_call_string)
    func_call = tree.body[0].value

    if isinstance(func_call, ast.Call):
        arguments = func_call.args

        arg_types = []
        for arg in arguments:
            arg_type = type(eval(ast.unparse(arg)))
            arg_types.append(arg_type)

        return arg_types

    return []
def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts
def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)


evalplus_type = "full"
evalplus_dict = {}
humaneval_dict = {}
evalplus_prompts = load_prompts(f"/home/frabbi/Documents/evalplus/{evalplus_type}.jsonl")
for prompt in evalplus_prompts:
    evalplus_dict[prompt['task_id']] = prompt
humaneval_prompts = load_prompts(f"../dataset-release/nominal/HumanEval.jsonl")
for prompt in humaneval_prompts:
    humaneval_dict[prompt['task_id']] = prompt


# gg = "assert ds7 == 9"
# print(exec(gg))
# exit()

# with open("/home/frabbi/Desktop/projects/evalplus/samples_eval_results.json", "r") as f:
#     result = json.load(f)
# for key in result["eval"].keys():
#     if result["eval"][key]["base"][0][0] != result["eval"][key]["plus"][0][0]:
#         print(key, " | HumanEval: ", result["eval"][key]["base"][0][0], " | ", "EvalPlus: ", result["eval"][key]["plus"][0][0])
        # print(result["eval"][key]["plus"][0][0])


check_difference_function = """
def check_difference(value1, value2):
    # return value1 == value2
    if isinstance(value1, str):
        return value1 == value2
    if isinstance(value1, (int, float)):
        if abs(value1) + abs(value2) == 0:
            return True
        relative_difference = abs(value1 - value2) / (abs(value1) + abs(value2))
        return relative_difference <= 0.01

    if isinstance(value1, list):
        if len(value1) != len(value2):
            return False
        for i in range(len(value1)):
            if not check_difference(value1[i], value2[i]):
                return False
        return True
    return value1 == value2
    if isinstance(value1, dict):
        if set(value1.keys()) != set(value2.keys()):
            return False
        for key in value1.keys():
            if not check_difference(value1[key], value2[key]):
                return False
        return True

    if isinstance(value1, map):
        return all(check_difference(x, y) for x, y in zip(value1, value2))

    return False
"""
# print(check_difference([.23,.4],[.23,.4]))
# exit()

py_result = {}

for task_id in humaneval_dict.keys():
    print(task_id)
    if task_id !="HumanEval/32":
        continue
    # # print(task_id)
    # py_result[task_id] = {"input":[], "evalplus_output":[], "humaneval_output":[]}
    evalplus_prompt = evalplus_dict[task_id]
    humaneval_prompt = humaneval_dict[task_id]



    evalplus_solution = evalplus_prompt['prompt']+evalplus_prompt["contract"]+evalplus_prompt["canonical_solution"]
    humaneval_solution = humaneval_prompt['prompt'] + humaneval_prompt["canonical_solution"]

    evalplus_test = check_difference_function + "\n"
    for t in evalplus_prompt['plus_input']:
        # evalplus_test += f"evalplus_function({str(t)[1:-1]})\n"
        # evalplus_test += f"humaneval_function({str(t)[1:-1]})\n"

        # evalplus_test += f"assert check_difference(humaneval_function({str(t)[1:-1]}), evalplus_function({str(t)[1:-1]}))\n"

        evalplus_test += f"if not check_difference(humaneval_function({str(t)[1:-1]}), evalplus_function({str(t)[1:-1]})):\n"
        evalplus_test += f"\tprint(\"Task ID: {task_id}\")\n"
        evalplus_test += f"\tprint(\"input:#\",{str(t)[1:-1]})\n"
        evalplus_test += f"\tprint(\"evalplus_output: \",evalplus_function({str(t)[1:-1]}))\n"
        evalplus_test += f"\tprint(\"humaneval_output: \",humaneval_function({str(t)[1:-1]}))\n"
        evalplus_test += f"\tprint(\"||\")\n"
        evalplus_test += f"\tprint()\n"

    # print(len(evalplus_prompt['plus_input']))

    if len(humaneval_prompt['entry_point']) < 3:
        evalplus_solution = evalplus_solution.replace(f"def {evalplus_prompt['entry_point']}(", f"def evalplus_function(")
    else:
        evalplus_solution = evalplus_solution.replace(f"{evalplus_prompt['entry_point']}","evalplus_function")

    if len(humaneval_prompt['entry_point']) < 3:
        humaneval_solution = humaneval_solution.replace(f"def {humaneval_prompt['entry_point']}(", f"def humaneval_function(")
    else:
        humaneval_solution = humaneval_solution.replace(f"{humaneval_prompt['entry_point']}","humaneval_function")



    full_code = evalplus_solution +"\n"+ humaneval_solution +"\n"+ evalplus_test
    # print(full_code)
    # exit()

    timeout = 4
    try:
        # print(task_id, end=": ")
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        # with stdoutIO() as s:
        print(exec(full_code))
        # py_result[task_id] = s.getvalue()
        signal.alarm(0)
        # print("Passed")
    except AssertionError as e:
        print(task_id, "Assertion Error")
    except (SyntaxError, TypeError) as e:
        print(task_id, "Compilation Error", e)
    except TimeoutError as e:
        print(task_id, "Timeout Error")
    except Exception as e:
        print(task_id, "Other Error",e)



    # print(full_code)
    # print("*"*50)
    # print(humaneval_solution)
    # print("*" * 50)
    # print(evalplus_test)
    # break

# with open("python_outputs.json", "w") as f:
#     json.dump(py_result, f, indent=4)
# print(py_result['HumanEval/49'])