# 1 and 3
import pandas as pd
import numpy as np

res1 = pd.Series("abcde")
res2 = pd.Series(["abcde"])
res3 = pd.Series( list("abcde") )
res4 = pd.Series('abcde')

# print(res2, res3)
print(res1 == res4)
