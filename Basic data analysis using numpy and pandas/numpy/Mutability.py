import numpy as np
import pandas as pd


#----------------------------------------------- changing index wise values of arrays (They are mutable).


arr=np.array([2,3,4,56,0])
arr[0]=99
print(arr)

two_D=np.array([

    [1,2,3],
    [4,9,0]

])


two_D[0][1]=9
print(two_D)