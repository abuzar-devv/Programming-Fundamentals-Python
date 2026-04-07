import pandas as pd
import openpyxl
import numpy as np

#Create a Pandas Series for marks of four students:
# Ali = 85, Sara = 92, Ahmed = 78, Fatima = 88
# Print the Series, Sara’s marks, and the average marks.




# data=pd.Series([85,92,78,88],index=["Ali","Sara","Ahmed","Fatima"])

# print(data)
# print(data["Sara"])
# print(data.mean())
















#Create a DataFrame with columns Name, Age, Department, and Marks for four students. Print the complete DataFrame.

# df=pd.DataFrame({
#     "Name":["Ali","Ahmed","Abuzar"],
#     "Age":[20,21,23],
#     "Department":["CS","MATH","PHYSICS"],
#     "Marks":[20,30,100]
# },index=["S1","S2","S3"])

# # print(df)
# # print(df[["Name","Marks"]])


# #Create a DataFrame with custom index labels S1, S2, S3, S4. Select:
# # row S2 using loc
# # first two rows using iloc


# # print(df.loc["S2"])
# # print(df.iloc[0:2])

# print(df[df["Department"]=="CS"])
# df["Grade"]=np.where(df["Marks"]>20,"A","B")
# print(df)









#Create a DataFrame with columns Name, Marks, and City. Rename Marks to Final_Marks.
# Then drop the City column.


# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed"],
#     "Marks": [85, 90, 78],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# })

# print(df)


# df=df.rename(columns={"Marks":"Final Marks"})
# df=df.drop("City",axis=1)
# print(df)










#Create a DataFrame where some marks are missing. Print missing value counts. Fill missing
# marks with the average marks.


# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
#     "Marks": [85, np.nan, 78, np.nan]
# })

# print(df)
# print(df.isnull().sum())
# print(df.fillna(df["Marks"].mean()))








#Create a DataFrame with duplicate student records. Remove duplicate rows and print the clean DataFrame.



# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ali", "Ahmed", "Sara"],
#     "Marks": [85, 90, 85, 78, 90]
# })


# print(df.duplicated())
# df=df.drop_duplicates()
# print(df)








#Create a student DataFrame and sort it by marks in descending order. Print the sorted DataFrame.


# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima"],
#     "Marks": [85, 90, 78, 95]
# })

# print(df.sort_values("Marks",ascending=False))









#Create a DataFrame with student names, departments, and marks. Find the average marks of each department.

# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hamza", "Ayesha"],
#     "Department": ["CS", "Math", "CS", "Math", "CS", "Math"],
#     "Marks": [85, 90, 78, 95, 88, 80]
# })

# print(df.groupby("Department")["Marks"].mean())











#Using a department and marks DataFrame, calculate mean, maximum, minimum, and count of marks for each department.

# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hamza", "Ayesha"],
#     "Department": ["CS", "Math", "CS", "Math", "CS", "Math"],
#     "Marks": [85, 90, 78, 95, 88, 80]
# })

# summary = df.groupby("Department")["Marks"].aggregate(["mean", "max", "min", "count"])

# print(summary)









#Create a small DataFrame, save it as students.csv, then read it back using pd.read_csv().
# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed"],
#     "Marks": [85, 90, 78],
#     "Department": ["CS", "Math", "CS"]
# })


# df.to_csv("Students.csv",index=False)

# read=pd.read_csv("Students.csv")











#Create one DataFrame with student IDs and names. Create another with student IDs and marks. Merge them using the ID column.

# First DataFrame (student info)
# df1 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["Ali", "Sara", "Ahmed"]
# })

# # Second DataFrame (marks info)
# df2 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Marks": [85, 90, 78]
# })

# merged=pd.merge(df1,df2,on="ID")
# print(merged)









#Create a DataFrame containing student departments. Count how many students are in each department using value_counts().

# df = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Hamza", "Ayesha", "Usman"],
#     "Department": ["CS", "Math", "CS", "Math", "CS", "Physics", "Math"]
# })

# print(df.value_counts("Department"))










#Create a DataFrame with product prices. Add a new column Discounted_Price by applying a 10% discount to each price.


# df = pd.DataFrame({
#     "Product": ["A", "B", "C", "D"],
#     "Price": [1000, 2000, 1500, 500]
# })


# df["Discounted Price"]=df["Price"]*0.90
# print(df)










#