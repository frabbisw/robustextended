import pandas as pd
import pickle

with open("data_with_robust.pkl", "rb") as f:
	data_with_robust = pickle.load(f)

print(len(data_with_robust))

print(len(data_with_robust[0]))
print(data_with_robust[0])
print()
print(len(data_with_robust[1]))
print(data_with_robust[1])
print()
print(len(data_with_robust[10]))
print(data_with_robust[10])
