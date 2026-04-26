import numpy as np
import pandas as pd


#-------------------------------------------------------flatten() and ravel()----------------------------------------------
# Both flatten() and ravel() give you a 1D version of the array, but the difference is how they store that 1D data in memory.

# arr=np.array([
#     [1,2,3],
#     [2,3,4]
# ])
c=np.array([1,2,3])
d=np.array([11,22,32])

a=c.flatten() #causing change in it will not have any impact on c 
b=d.ravel() #causing change in b might also change d

a[0]=99   
b[0]=20   
print(c)
print(d)






# mat = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# print(mat.flatten())
# print(mat.ravel())
