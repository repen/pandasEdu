# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd
import numpy as np
import re

# data_set = pd.read_csv("data/tr_types.csv", delimiter=";", nrows=10000)
data_set = pd.read_csv("data/transactions.csv", delimiter=",", nrows=10000)
# data_set = pd.read_csv("data/transactions.csv", delimiter=",", )
my_data_set = pd.DataFrame([ ["42",2,3], ["33",2,3],["33",3,4], ["22", 2,3]])

# print(my_data_set)
# res = data_set.groupby("tr_type").nunique()
# print( res)
# r = data_set.tr_description.describe()
# print(r)
# data_frame = data_set.sample( 100, random_state= np.random.seed( 242 ) )
# r = my_data_set[0].value_counts().loc[lambda x: x > 1]
# r = my_data_set[0].value_counts()
# print(r)
# data_set.va
r = data_set.tr_type.value_counts()[-5:]
print(r)
