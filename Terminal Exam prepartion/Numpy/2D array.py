import pandas as pd
import numpy as np



# arr=np.array([

#     [1,2.1,3,4],
#     [2,1,3,4],
#     [1,2,2,3]

# ])

# print(arr.shape) # (3,4) -----> (3 rows , 4 columns)
# print(arr.ndim)  # Gives the number of dimensions
# print(arr.size)  # no of elements
# print(arr.dtype) #Data type of array --------> if one entry is float then whole becomes float --------> must have same dtype throughout array




#------------------------------------------------------- Indexing and changing values--------------------

arr=np.array([

    [2,3,4,5],
    [2,1,3,4],
    [0,3,1,2],
    [0,1,3,1]

])

arr[0][1]=99
print(arr)

# mat = np.array([[1, 2], [3, 4]])
# mat[1, 0] = 100
# print(mat)



# print(arr[0:2,0:2])
# print(arr[-1::-1,-1:-3:-1])