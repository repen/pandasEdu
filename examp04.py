import pandas as pd
import numpy as np

np.random.seed(123)
series = pd.Series( np.random.normal(size=100) )
series.index.rename(0, "sss")
# ns = series.apply( lambda x: x ** 3)

print(series)
# print(ns)
ne = pd.Series( [[1,2,3,4], [1,2,3,4]] )
print(ne)