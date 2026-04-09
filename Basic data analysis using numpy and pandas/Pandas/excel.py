import openpyxl
import pandas as pd




df=pd.read_excel("DataFrame.xlsx")

df.to_excel("output.xlsx",index=False)

# print(df.head()) #gives 1st 5 rows 
# print(df.tail()) #gives last 5 rows
# print(df.shape) #gives shape of xlsx file 
# print(df.columns) #gives column names
# print(df.dtypes) #gives data type of columns



#Getting information about file before starting analysis

print(df.info())
print(df.describe()) #gives statistical summary for numerical columns.
