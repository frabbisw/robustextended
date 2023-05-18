# get the result from https://www.kaggle.com/frabbisw/mpnet

import pickle

with open("result_dict", "rb") as f:
    result_dict = pickle.load(f)

augs = {}
for lang in result_dict.keys():
    docstring = result_dict[lang]["entry"]
    for aug in docstring.keys():
        sim = docstring[aug]
        if aug not in augs.keys():
            augs[aug] = []
        augs[aug].append(round(sim,2))

for aug in augs.keys():
    print(f"Function & {aug} ", end="")
    for v in augs[aug]:
        print(f"& {v} ", end="")
    print("\\\\")

augs = {}
for lang in result_dict.keys():
    docstring = result_dict[lang]["doc"]
    for aug in docstring.keys():
        sim = docstring[aug]
        if aug not in augs.keys():
            augs[aug] = []
        augs[aug].append(round(sim,2))
for aug in augs.keys():
    print(f"docString & {aug} ", end="")
    for v in augs[aug]:
        print(f"& {v} ", end="")
    print("\\\\")