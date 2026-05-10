import numpy as np
import pandas as pd

# zero=np.zeros((2,2))
# one=np.ones((9,2))
# full=np.full((5,4),9)

# print(f"0: {zero} , 1:{one}, full:{full}")






# Create a 3 x 3 matrix filled with zeros then inquire for students marks and customize the matrix with student marks

# dummy=np.zeros((3,3))

# for rows in range(3):
#     for columns in range(3):
#         marks=float(input("Enter marks:"))
#         dummy[rows][columns]=marks

# print(f"Final marks are = {dummy}")




# in numpy code 

marks=np.array([float(input("Enter marks:")) for _ in range(9)])
marks=marks.reshape(3,3)
print(marks)

