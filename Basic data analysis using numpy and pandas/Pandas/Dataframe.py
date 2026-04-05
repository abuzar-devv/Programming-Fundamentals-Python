import pandas as pd


#It is 2D data structure

# data=pd.DataFrame({

#     "Name":["abuzar","ali","hamza","safi","hammad"],
#     "Marks":[10,20,80,7,0],
#     "grade":["A","B","A","C","B"],
#     "Age":[20,21,3,19,121]

# },index=[22,21,34,56,71])

# # # print(data)
# # 
# # print(data.loc[21])    #we can use .loc for searching by row lable only
# # 
# # print(data["Name"])       #For column search use this

# print(data[data["Marks"] > 20]) #filtering bu column




#------------------------------------------------List of dictionaries-----------------------------------

# Each dictionary has data of a single student

students = [
    {"Name": "Ali", "Age": 20, "Score": 85},
    {"Name": "Sara", "Age": 21, "Score": 90},
    {"Name": "Ahmed", "Age": 19, "Score": 78}
]

df = pd.DataFrame(students)
print(df)



