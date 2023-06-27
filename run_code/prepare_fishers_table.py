import pandas as pd;
from scipy.stats import fisher_exact
import numpy as np

sample_size = 164

df = pd.read_csv("../R/stat.csv", sep=",", skipinitialspace=True)
df = df.reset_index()

models_dict = {}

for index, row in df.iterrows():
    if row["model"] not in models_dict.keys():
        models_dict[row["model"]] = {}
    if row["language"] not in models_dict[row["model"]].keys():
        models_dict[row["model"]][row["language"]] = {}
    if row["method"] not in models_dict[row["model"]][row["language"]].keys():
        models_dict[row["model"]][row["language"]][row["method"]] = [row["Passed"], row["Assertion"], row["Compilation"], row["Timeout"], row["Runtime"]]

def get_pvalue(method_error_rates, nominal_error_rates):
    pm = method_error_rates[0] * sample_size/100
    pn = nominal_error_rates[0] * sample_size/100
    fm = sum(method_error_rates[1:]) * sample_size/100
    fn = sum(nominal_error_rates[1:]) * sample_size/100
    table = np.array([[pn,fn],[pm,fm]])
    # print(table)
    res = fisher_exact(table, alternative='two-sided')
    return round(res.pvalue, 3)



for model in models_dict.keys():
    for lang in models_dict[model].keys():
        for method in models_dict[model][lang].keys():
            if method in ["Nominal", "Partial"]:
                continue
            method_error_rates = models_dict[model][lang][method]
            if method in ["Syntax", "Format"]:
                nominal_error_rates = models_dict[model][lang]["Partial"]
            else:
                nominal_error_rates = models_dict[model][lang]["Nominal"]
            pvalue = get_pvalue(method_error_rates, nominal_error_rates)
            print(model, lang, method, pvalue)



# for index, row in df.iterrows():
#     if row["method"] is not ["Nominal", "Partial"]:
#         method_error_rates = models_dict[row["model"]][row["language"]][row["method"]]
#             if row["method"] in ["Syntax", "Format"]:
#                 nominal_error_rates =
#         models_dict[row["model"]][row["language"]][row["method"]] = [row["Passed"], row["Assertion"], row["Compilation"], row["Timeout"], row["Runtime"]]

# print(models_dict)
