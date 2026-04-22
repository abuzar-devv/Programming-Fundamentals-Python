import numpy as np
import pandas as pd


#
# 
# 
# ------------------------------------------ combining arrays ----------------------------

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate([a,b]))  



x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(np.vstack([x, y])) 
print(np.hstack([x, y]))








# x=np.array([1,2,3])
# y=np.array([4,5,6])
# print(np.concatenate([x,y]))
# print(np.hstack([x,y]))
# print(np.vstack([x,y]))







# #Gemini practice



# #Ticket 1: The Database Appender (Vertical Integration)
# # The Scenario:
# # You are maintaining a database of employee records. Your current matrix has 3 employees, each with 4 attributes (Age, Salary, Tenure, Performance).
# # A new employee is hired, and their data arrives as a flat 1D array.

# # # Current Database: (3, 4)

# # employees = np.array([
# #     [25, 60000, 2, 85],
# #     [30, 85000, 5, 92],
# #     [45, 120000, 10, 88]
# # ])

# # # New Hire Data: (4,)
# # new_hire = np.array([28, 70000, 1, 90])


# # Your Business Requirement:
# # Use np.vstack to add the new_hire to the bottom of the employees matrix. Print the final (4, 4) matrix.



# # employees = np.array([
# #     [25, 60000, 2, 85],
# #     [30, 85000, 5, 92],
# #     [45, 120000, 10, 88]
# # ])
# # new_hire = np.array([28, 70000, 1, 90])

# # print(np.vstack([employees,new_hire]))









# # #Ticket 2: The Feature Engineering Crash (The Dimension Trap)
# # The Scenario:
# # You are preparing data for an AI model. You have a matrix of 5 users with 3 features each.
# # Your data science team has calculated a brand new "Risk Score" for these 5 users.

# # Python
# # import numpy as np

# # # User Data: (5, 3)
# # user_data = np.array([
# #     [10, 20, 30],
# #     [15, 25, 35],
# #     [12, 22, 32],
# #     [18, 28, 38],
# #     [11, 21, 31]
# # ])

# # # Risk Scores: (5,)
# # risk_scores = np.array([99, 45, 88, 23, 76])
# # Your Business Requirement:
# # You must add the risk_scores as a 4th column on the right side of user_data using np.hstack.
# # Warning: If you simply write np.hstack([user_data, risk_scores]), your program will instantly crash with a ValueError because the dimensions are physically incompatible.
# #  You must mathematically alter the geometry of risk_scores first so that it legally binds to the 2D matrix. Print the final (5, 4) matrix.




# user_data = np.array([
#     [10, 20, 30],
#     [15, 25, 35],
#     [12, 22, 32],
#     [18, 28, 38],
#     [11, 21, 31]
# ])

# risk_scores = np.array([99, 45, 88, 23, 76])
# risk_scores=risk_scores.reshape(5,-1)
# print(risk_scores)
# print(np.hstack([user_data,risk_scores]))










#Ticket 2 (Revised): The Frankenstein Tensor

# The Scenario:
# You are building an empty architectural framework for a neural network. You are not given any existing data.
#     You must generate the memory blocks natively and assemble them.

# Your Business Requirement:
# Construct and print a final (3, 4) matrix that matches these exact physical specifications:

# The top-left 2x2 sector must be entirely zeros.

# The top-right 2x2 sector must be entirely ones.

# The entire bottom row (spanning across all 4 columns) must be filled with the number 9.

# The Constraint: You cannot manually type out a Python list of these numbers.
# You must use NumPy generation functions to create the components, and NumPy stacking functions to glue them together into the final (3, 4) shape.





zero=np.zeros((2,4))
nine=np.full((4,),9)
new_array=np.vstack([zero,nine])
print(new_array)