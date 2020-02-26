# 1.13
import pandas as pd
import numpy as np

series = pd.Series(np.linspace( 0, 20, 15 ))

result_array = []
for i, num in enumerate( series ):
    if i > 1:
        res = series[i] / series[i-1]
        print(series[i], "/", series[i-1], "=", res)
        result_array.append( res )
    elif i == 1:
        print(series[i], "/", series[i-1], "=", "inf")
    elif i == 0:
        print(series[i], "/", "NaN", "=", "NaN")

print("Result: ",result_array)
result_array = list( filter( lambda x: x < 1.5, result_array) )

print("Result filter: ", result_array)
average = sum(result_array) / len(result_array)
print(average)
