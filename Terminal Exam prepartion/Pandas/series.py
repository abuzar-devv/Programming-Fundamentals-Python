import pandas as pd
import numpy as np

marks=pd.Series([20,30,40,50],index=["a","b","c","d"])
print(marks)
print(marks["a"])
print(marks[marks>20])


