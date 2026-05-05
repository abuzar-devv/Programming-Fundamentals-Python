import numpy as np
import pandas as pd 

marks = np.array([78, 85, 62, 90, 55, 88, 73])

# print(marks.max())
# print(marks.mean())
# print(marks.std())
# print(marks.min())




# matrix=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(matrix[1:2,-1:])
# print(matrix[0])
# print(matrix[-1])
# print(matrix[0::,1])


# arr=np.arange(1,10)
# new_arr=arr.reshape(3,3)
# print(np.sum(arr))
# print(np.sum(new_arr,axis=1))
# print(np.sum(new_arr,axis=0))




import random
import numpy as np
#Generate a 4 by 4 matrix of random integers from 1 to 20. Print:
# the matrix
# maximum value in each row
# minimum value in each column
# Use a random seed so the output is repeatable.

np.random.seed(9)
matrix=np.random.randint(1,21,size=(4,4))
print(matrix)
print(np.min(matrix,axis=1)) #-----------> Row
print(np.max(matrix,axis=0)) #-----------> Column