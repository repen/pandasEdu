# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
import pandas as pd
import numpy as np
import re

data_set = pd.read_csv("data/transactions.csv", delimiter=",", nrows=1000)

ds = data_set.set_index("customer_id")
# print(ds)
res = ds[ ds['amount'] == ds['amount'].max() ]
ds2 = data_set[ data_set["customer_id"] == 39026145]
# print( ds2 )
ds2['amount'] = ds2['amount'].astype(str)
ds2 = ds2['amount'].apply( lambda x:x.replace("-","") )
ds2 = ds2.astype(float)
# print( type( ds2 ) )
top = ds2.value_counts()
top = top[ top > 1 ]
print( top.head() )

# print( ds2 )
