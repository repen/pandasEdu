# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd
import numpy as np
import re

d = 1000000
df1 = pd.read_csv("data/transactions.csv", delimiter=",", nrows=d)
df2 = pd.read_csv("data/tr_mcc_codes.csv", delimiter=";", nrows=d)
df3 = pd.read_csv("data/tr_types.csv", delimiter=";", nrows=d)
df4 = pd.read_csv("data/gender_train.csv", delimiter=",", nrows=d)
# print(df1)
# new_pd = pd.merge(df1, df2, df3)
df1 = df1.merge( df2 )
df1 = df1.merge( df3 )
df1 = df1.merge( df4, how="left" )

fdf1 = df1[ df1.amount < 0 ]
gender0 = fdf1[fdf1.gender == 0]
gender1 = fdf1[fdf1.gender == 1]
# print(gender0.mean())
print("==========+")
f = [ gender0.mean().amount, gender1.mean().amount]
res = np.ptp( f )
print(res)

# df_combined.to_csv(combined_file_name)



# data_set = pd.read_csv("data/transactions.csv", delimiter=",", nrows=1000000)
