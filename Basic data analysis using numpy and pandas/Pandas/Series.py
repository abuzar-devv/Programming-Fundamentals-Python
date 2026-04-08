import pandas as pd 

# print(pd.__version__)


#----------------------------------------------------------------------------Series (1D)-----------------------------------------------------------------------------------------------------

import string

marks=pd.Series([20,30,40,50,79])  # it will make the column of data , each with its lablel which is index by default but can be changed 
print(marks)



data=pd.Series([10,20,30],index=["a","b","c"])
data["a"]=200
print(data)
# we can acces values by their custom labels

# print(data.loc["a"])


# adding condition


large_data=pd.Series([20,30,19,34,9,12,45,67])
print(large_data[large_data>=20])

