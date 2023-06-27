import pandas as pd;

df = pd.read_csv("../R/stat.csv", sep=",", skipinitialspace=True)
df = df.reset_index()

# methods = ["Nominal", "Partial", "Function", "DocString", "Syntax", "Format"]
errors = ["Passed","Assertion","Compilation","Timeout","Runtime"]

# print(df.columns)

# for index, row in df.iterrows():
#     print(row['method'])
#     break

methods_dict = {}
#
# print(df)

for index, row in df.iterrows():
    if row["method"] not in methods_dict.keys():
        methods_dict[row["method"]] = {}

    for error in errors:
        if error not in methods_dict[row["method"]].keys():
            methods_dict[row["method"]][error] = []
        methods_dict[row["method"]][error].append(row[error])

for method in methods_dict.keys():
    row = methods_dict[method]
    flag = 0
    for error in row.keys():
        if flag:
            print(f"\t& {error} ", end="")
        else:
            print("\t\\multirow{5}{*}{\\centering method} & error ".replace("method",method).replace("error",error), end="")
        flag = 1
        for e in row[error]:
            print(f"& {e} ", end="")
        print("\\\\")
    print("\t\\hline")
