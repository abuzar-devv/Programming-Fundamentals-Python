import numpy as np
import pandas as pd


#---------------------------------- Axis in numpy-----------------------------


# --------------------------------- Axis = 0 (vertical operation)-----------------

#------------------------------------axis = 1 (Horizontal operation)--------------------


arr = np.array([
    [12, 7, 9],
    [5, 15, 3],
    [20, 8, 11]
])

print(np.sum(arr,axis=0)) #Performed vertical operation (moving top to bottom row wise)
print(np.sum(arr,axis=1))  #Performed horizontal operation (moving left to right column wise)






