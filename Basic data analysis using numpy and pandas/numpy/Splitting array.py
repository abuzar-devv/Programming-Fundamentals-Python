import numpy as np
import pandas as pd



# #---------------------------------------------------------------------- splitting array---------------------------------------------------------------------------

arr=np.array([

    [2,3,4,5,6],
    [1,2,4,6,8],
    [0,1,4,5,7]

])
print(np.split(arr,5,axis=1))
print(np.split(arr,3,axis=0))



# a=np.array([1,2,3,4,5,6])
# print(np.split(a,6)) # split into 6 equal parts .



#--------------------------------------------------------------Gemini---------------------------------------------



#Ticket 1: The Train/Validation/Test Pipeline (The Scalpel)
# The Scenario:
# You are feeding data into a Machine Learning model. You have a dataset of 10 samples (rows).
# Standard AI pipelines require you to split your data into three specific sets: one for training the model, one for validating it, and one for testing it.


# # Shape: (10, 4)
# # 10 Samples, 4 Features each
# ml_data = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20],
#     [21, 22, 23, 24],
#     [25, 26, 27, 28],
#     [29, 30, 31, 32],
#     [33, 34, 35, 36],
#     [37, 38, 39, 40]
# ])
# Your Business Requirement:
# You must shatter this (10, 4) matrix horizontally (row-wise) into exactly three separate matrices:

# train_set: The first 6 rows.

# val_set: The next 2 rows.

# test_set: The final 2 rows.

# You are restricted to using a single NumPy splitting function and the "Scalpel Rule" (an array of cut indices) in one line of code. Print the .
# shape of all three resulting matrices.



# Solution

# 10 Samples, 4 Features each

# ml_data = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20],
#     [21, 22, 23, 24],
#     [25, 26, 27, 28],
#     [29, 30, 31, 32],
#     [33, 34, 35, 36],
#     [37, 38, 39, 40]
# ])


# print(np.array_split(ml_data,3))


