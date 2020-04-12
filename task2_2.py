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

# print(df1.keys())
# print( df1.mcc_code )

tr_type = df1.tr_type.astype( str )
mcc     = df1.mcc_code.astype( str )
new = tr_type + mcc
df1.insert(2, "New", new)
count = df1.tr_description.value_counts()
count = count[10 < count]

# print(count)
# df1 = df1[ df1.tr_description.str.contains("POS", regex=True) ]
df1 = df1[ df1["tr_description"].isin( count.index ) ]
print(df1.keys())

df1_minus = df1[ df1.amount < 0 ]
df1_minus.New = df1_minus.New.astype(int)
dis = df1_minus.New.std( )
print(dis)
