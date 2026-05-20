import pandas as pd
import numpy as np

df=pd.DataFrame({

    "name":["ali","ahmad","abuzar","Musa"],
    "Age":[20,19,18,21],
    "Marks":[80,69,99,90],
    "Grade":["A","B","A+","A"]

},index=[1,2,3,4])

# print(df)

# print(df[["name","Age"]])

print(df[(df["Marks"]>80) & (df["Age"]>18)])

