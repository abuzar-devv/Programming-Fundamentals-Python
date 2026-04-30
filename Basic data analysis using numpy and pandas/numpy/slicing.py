import numpy as np
import pandas as pd



#---------------------------- Slicing------------------------------------------


#------------------ 2D

#In a 2D NumPy array: Every row must have the same number of elements

# arr=np.array([

#     [1,2,3,4,5],
#     [1,9,0,1,10],
#     [99,0,1,2,4],
#     [11,13,2,1,4]

# ])

# print(arr[::-1])
# print(arr[0])  # row 0

# # Column selection 
# print(arr[0:5:2,0:6:2])             # general structure(row slicing (start:stop(excluded):step) , column slicing (start:stop(excluded):step))












# ------------------------------------------------#Slicing practice (2D)

# arr=np.array([

#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]

# ])

# # print(arr[0:2,1:3])
# # print(arr[0:,-1:])
# # print(arr[-1:-3:-1 , -1:-3:-1])
# # print(arr[0::2,0::2])
# # print(arr[0:3,1:4])
# # print(arr[-1:-3:-1,-3:-5:-1])
# # print(arr[::-1,::-1])
# # print(arr[1:3,1:3])
# # print(arr[2:3,0:])
# # print(arr[0::2,0::2])
# # print(arr[1:,0:3])