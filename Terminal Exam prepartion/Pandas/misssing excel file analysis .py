import pandas as pd
import numpy as np
import openpyxl


#----------------------------------------- Loading file for analysis

df=pd.read_excel("missing.xlsx")

# print(df)
# print(df.info())
# print(df.describe())


#---------------------------------------------- Simple functions

# print(df.head()) # first 5 rows
# print(df.tail()) # last 5 rows
# print(df.shape) # rows and columns
# print(df.columns) # column names
# print(df.dtypes) 


#---------------------------> Selecting columns , iloc and loc

# print(df[["Name","Marks","Department"]])

# print(df.loc[0:10,["Name","Marks"]])
# # print(df.iloc[0:100:10,::-1])


# print(df[["Marks","Name"]])




#-----------------------> Adding new column

# df["Bonus marks"]=df["Marks"]+10
# print(df["Bonus marks"])
# print(df)




#--------------------------> Clipping()

# df["Marks"]+=2
# df["Marks"]=df["Marks"].clip(upper=100)  # sets a upper limit , values cannot exceed 100 after operationt







#-------------------------------> Sorting()

# print(df.sort_values(["Marks","Department"],ascending=[False,True]))








#--------------------------------Missing values

# print(df.isnull())
# print(df.isnull().sum())






#=================> Handling Missing values



# print(df.dropna())

# avg=df["Marks"].mean()
# df["Marks"]=df["Marks"].fillna(avg)
# print(df)








#-------------------------------------------> Rename ()
# df = df.rename(columns={
#     "Name": "New Name",
#     "Marks": "Score"
# })

# print(df)





#---------------------------------> Total unique value count in each row

# print(df["Department"].value_counts())
# print(df["Marks"].value_counts())





#-------------------------------------> Dates 



# data = pd.DataFrame({

#     "Date": ["2026-01-05", "2026-01-06", "2026-01-07"],
#     "Sales": [1200, 1500, 900],
#     "Month":["Jan","feb","Jul"]

# })

# data["Date"]=pd.to_datetime(df["Date"])
# df["Month"] = df["Date"].dt.month









#---------------------------- numpy in pandas


df["Result"]=np.where(df["Marks"]>=50,"Pass","Fail")
print(df)
