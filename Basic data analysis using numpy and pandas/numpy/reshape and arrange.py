import numpy as np
import pandas as pd


#------------------------------------------------------------------reshape array  and arange ------------------------------------------------------------------------


# arr=np.arange(1,13)     #np.arange(start, stop, step, dtype=None) , ending value is excluded
# print(arr)

# arr2=np.arange(0,100,10,dtype=float)
# print(arr2)



#Rule for reshaping : no of rows x no of columns = size of array 


# arr=np.arange(1,13)     
# reshaping=arr.reshape(3,4)          #(rows,columns)
# reshaping_2=arr.reshape(2,6)
# reshaping_3=arr.reshape(4,3)
# print(reshaping)







# Gemini practice











#Ticket 1: The Countdown Matrix (Reverse Generation & Dynamic Reshaping)
# Your Business Requirement:

# Use np.arange() to generate a flat 1D sequence of numbers starting exactly at 100 and counting down to 10 (inclusive), in steps of -10.

# Reshape this array into a 2D matrix that strictly has 2 rows. You must use the -1 wildcard to force NumPy to dynamically calculate the number of columns.

# Print the final matrix




# arr=np.arange(100,0,-10)
# new_shape=arr.reshape(-1,5) # -1 means i want 5 columns strictly , manage the rows yourself what ever fits here accordingt to the size of array
# new_shape=arr.reshape(2,-1) # means i want 2 rows , manage columns yourself
# print(new_shape)


# In reshape(), -1 tells NumPy to automatically calculate that dimension based on total elements.







#Ticket 2: The 3D Video Tensor (Generation & Multi-Dimensional Reshaping)
# Your Business Requirement:

# Use np.arange() to generate a flat 1D sequence of exactly 60 consecutive integers starting from 0.

# You are allocating memory for a short video file. Reshape this flat sequence into a 3-dimensional tensor representing 3 frames of video,
#     where each frame has a pixel resolution of 4 rows and 5 columns.

# Print the .shape attribute of the resulting tensor to prove it successfully formatted to (3, 4, 5).


# arr=np.arange(0,60)
# new_shape=arr.reshape(3,4,5)
# print(new_shape)



