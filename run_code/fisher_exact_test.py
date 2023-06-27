# # importing packages
# import scipy.stats as stats
# from scipy.stats import fisher_exact
# import numpy as np
# import pandas as pd
#
# df = pd.read_csv("stat.csv", skipinitialspace=True)
# # print(df.head())
#
# js6b = df[df["model"]=="codegen6bmulti"]
# js6b = js6b[js6b["language"]=="js"]
#
# # js6b = js6b[['passed', 'assertion', 'compilation', 'timeout', 'runtime']]
# js6b = js6b[['passed', 'assertion']]
# js6b = js6b.to_numpy()
#
# res = fisher_exact(js6b[0:2], alternative='two-sided')
#

import numpy as np
from scipy.stats import fisher_exact

# Create the 2x5 matrix
matrix = np.array([[10, 15, 20, 25, 30],
                   [5, 10, 15, 20, 25]])

# Perform Fisher's exact test
odds_ratio, p_value = fisher_exact(matrix)

# Print the results
print("Odds Ratio:", odds_ratio)
print("P-value:", p_value)