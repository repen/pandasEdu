import pandas as pd
import numpy as np

np.random.seed(242)

series = pd.Series( np.random.normal( size=100 ) )
series = series ** 3

series.index = series.index.map( lambda x : x * 3)

a1 = series[ (series < 2.6) & (series.index % 2 == 1) ]
print(a1.sum()) # -15.150748101821666
a2 = series[ series < 0]
print( a2.count() ) # 51
print( a2.describe() )

