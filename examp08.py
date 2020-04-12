# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd
import numpy as np
import re

data_set = pd.read_csv("data/transactions.csv", delimiter=",", nrows=1000000)

# ds = data_set.set_index("customer_id")
# res = ds[ ds['amount'] == ds['amount'].max() ]
print(data_set)

mediana = data_set['amount'].median()
print("First:", mediana)

data_set02 = data_set[  data_set["term_id"].notnull() ]
mediana2 = data_set02['amount'].median()
print("Second:", mediana2)

data_set03 = data_set.drop_duplicates(subset=["mcc_code", "tr_type"], keep="last")
mediana3 = data_set03["amount"].median()
print("Three:", mediana3)
r = [mediana, mediana2, mediana3]

res = np.ptp(r)

print(res)