import pandas as pd
import openpyxl

df=pd.read_excel("DataFrameMissing.xlsx")



df.to_excel("output.xlsx", index=False)

#----------------------------------------------------------------------basic functions---------------------------------------------------



# print(df.head()) #gives 1st 5 rows 
# print(df.tail()) #gives last 5 rows
# print(df.shape) #gives shape of xlsx file 
# print(df.columns) #gives column names
# print(df.dtypes) #gives data type of columns






#-------------------------------------------------------------------Getting information about file before starting analysis----------------------------



# print(df.info())  # gives quick summary of file
# print(df.describe()) #gives statistical summary for numerical columns.
# print(df["Age"])




# printing different columns give a data frame
# print(df[["Age","Marks"]])








#-----------------------------------------------------printing by lables--------------------------------


# print(df.loc[0:11])








#------------------------------------------------loc and iloc-----------------------------------------------


# we can also get custom columns and rows



# print(df.loc[100:200,["Marks","Age"]])   #loc is label based 

# print(df.iloc[0:20,0:2])   #iloc is index based 









#----------------------------------------------------------Filtering data---------------------------------------------------------

# cs_students = df[df["Department"] == "Computer Science"]
# print(cs_students.describe())

# high_achievers=df[df["Marks"]>70]
# print(high_achievers)
# print(high_achievers.info())
# print(high_achievers.describe())


# with multiple conditions

# CS_high_achievers=df[ (df["Department"]=="Computer Science") & (df["Marks"]>95) ]
# print(CS_high_achievers)
# print(CS_high_achievers.info())
# print(CS_high_achievers.describe())










#-------------------------------------------------------------------- creating new column---------------------
# df["Bonus"]=5
# df["Final"]=df["Marks"] + df["Bonus"]
# print(df.head())








#--------------------------------------------------------------- using clip()-------------------------------------------------
# df["Marks"]=df["Marks"].clip(upper=90)   # make values above 90 as 90
# print(df["Marks"].describe())











#------------------------------Deleting column-----------------------------------\\


# new_df=df.drop(columns=["Marks"])  #$ it copies column from old data frame to new one
# print(new_df)

# df.drop(columns=["Marks"], inplace=True)









#-------------------------------sorting--------------------------------------------------


# print(df.sort_values("Marks",ascending=False))   #in descending order
# print(df.sort_values("Marks")) 






#------------------------------Missing data------------------------------------------

# print(df.isnull())  # returns true/false output
# print(df.isnull().sum()) # returns no of nan values in eachj column








#----------------------------------------- handling missing data -------------------------------------

# clean_file=df.dropna()


# # fill missing values 

# df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
# print(df.info())










#--------------------------------------------------- Renaming columns----------------------------------------

# df=df.rename(columns={
#     "Marks": "Score",
#     "Department":"School"
# })

# print(df.info())







#---------------------------------------------------------Value count--------------------------------------

# print(df.value_counts(["Department"]))
# print(df.value_counts(["Name"]))











#--------------------------------------------------------------------groupby() -----------------------------------------------

#It provides catgoically summaries based upon input
# General form :  df.groupby('category_column')['numeric_column'].function()


# avg=df.groupby("Department")["Marks"].mean()

# # maximum and minimum ages in department catigorically
# max_age=df.groupby("Department")["Age"].max()
# min_age=df.groupby("Department")["Age"].min()
# print(avg)
# print(max_age)
# print(min_age)









#--------------------------------------------------------------Multiple aggregation-------------------------------------------

#it is used when we want more fruightful insigts from the data previously we wanted max or min or avg from each departmentg now we can get thrice 

#General structure: df.groupby("Category_column").aggregate({
   #                         "Column_name" : [Required calulations]
#                                           
                                                    #})



# summary=df.groupby("Department").aggregate({
#     "Marks":["mean","max","min","count"],
#     "Age":"mean"
# })

# print(summary)













#--------------------------------------------------- grouping by more than 1 column-------------------------------------
summary=df.groupby(["Department","Age"])["Marks"].mean()
print(summary)










#-------------------------------------------------------Working with dates-------------------------------------------------------

# data=pd.DataFrame({
#     "Date":["2026-01-05","2026-01-06","2026-01-07"],
#     "Sales":[20000,18000,25000]
# })

# data["Date"]=pd.to_datetime(data["Date"])
# data["Month"]=data["Date"].dt.month
# data["Month"]=data["Date"].dt.day_name()
# print(data)





