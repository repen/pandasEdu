# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd
import numpy as np
import re

data_set = pd.read_csv("data/tr_types.csv", delimiter=";")


# print(data_set)
data_frame = data_set.sample( 100, random_state= np.random.seed( 242 ) )
# print(data_frame)
res = data_frame[ data_frame['tr_description'].str.contains( r"\bплата", regex=True, case=False) ]
print( res.pct_change )
# print(res.describe())





