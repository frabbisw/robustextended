# import os
# import pandas as pd
# import numpy as np
# result_dir = "../datasets/result"
# langs = ["java", "cpp", "js"]
# K = 10
# dataframes = []
# for lang in langs:
#     filepath = os.path.join(result_dir, f"{lang}_K_{K}.csv")
#     df = pd.read_csv(filepath)
#     # df.loc['total'] = df.iloc[1:].sum()
#     df.loc[lang] = df.iloc[1:].sum()/df.sum()
#     df = df.iloc[-1:]
#     dft = df.T.iloc[1:]
#     dft.index.name = "Method Name"
#     # print(dft.columns)
#     dft.to_csv("../datasets/result/sample.csv")
#     dft = pd.read_csv("../datasets/result/sample.csv")
#     dataframes.append(dft)
#     dft['Method Name'] = dft['Method Name'].str.replace(f"{lang}_","")
#     # print(dft)
#
# merged_df = dataframes[0]
# for i in range(1, len(dataframes)):
#     merged_df = pd.merge(merged_df, dataframes[i], on="Method Name", how="outer")
#
# # merged_df["Method Type"] = merged_df["Method Name"]
# merged_df["Method Type"] = merged_df["Method Name"].str.split("_").str[0]
# merged_df = merged_df[["Method Type", "Method Name", "java", "cpp", "js"]]
# merged_df["go"] = np.nan
# merged_df = merged_df.round(2)
#
#
# prev = ""
# for index, row in merged_df.iterrows():
#     if prev != row['Method Type']:
#         print("\\hline")
#     print(f"{row['Method Type']} & {row['Method Name']} & {row['java']} & {row['cpp']} & {row['js']} & {row['go']} \\\\".replace("_","\\_"))
#     prev = row['Method Type']
# print("\\hline")
# # print(merged_df)