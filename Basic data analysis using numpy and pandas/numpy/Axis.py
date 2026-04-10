import numpy as np
import pandas as pd


#---------------------------------- Axis in numpy-----------------------------


# --------------------------------- Axis = 0 (vertical operation)-----------------

#------------------------------------axis = 1 (Horizontal operation)--------------------


# arr = np.array([
#     [12, 7, 9],
#     [5, 15, 3],
#     [20, 8, 11]
# ])

# print(np.sum(arr,axis=0))  #Performed vertical operation (moving top to bottom row wise)
# print(np.sum(arr,axis=1))  #Performed horizontal operation (moving left to right column wise)



# # computing mean


# arr=np.array([
#     [1,2,3],
#     [2,3,1],
#     [9,0,2]
# ])


# print(np.mean(arr,axis=0)) #compute column calculation moving top to bottom row wise . it is a vertical operation
# print(np.mean(arr,axis=0))  #Compute rows calculation moving left to right column wise . it is horizontal operation.







#There are stock prices every day top to bottom calculate standard deviation vertically if std is > 5 consider it high.


# stocks = np.array([
#     [45, 46, 21],
#     [42, 10, 99],
#     [46, 123, 500],
#     [39, 870, 1],
#     [42, 770, 65],
#     [37, 5, 391],
#     [47, 674, 10005]
# ])

# # Step 1: volatility (risk) per stock (column-wise)
# risk = np.std(stocks, axis=0)

# # Step 2: use relative threshold (more meaningful than fixed number)
# threshold = np.mean(risk)

# # Step 3: classification
# analysis = np.where(risk > threshold, "High risk", "Low risk")

# print("Risk per stock:", risk)
# print("Threshold:", threshold)
# print("Analysis:", analysis)








# Gemini practice 

# Ticket 1: The Logistics Bottleneck
# The Scenario:
# You are managing the warehouse inventory for a logistics company. You have 5 warehouses, and each warehouse stocks the exact same 4 products. 
# The data is provided as a (5, 4) matrix.


# Your Business Requirements:

# The CEO wants to know the average stock level of each specific product across the entire company. Output an array of 4 numbers.

# The CEO wants to know the total combined inventory of each specific warehouse to see which one is the emptiest. Output an array of 5 numbers.


# # Rows: 5 Warehouses
# # Columns: 4 Products
# inventory = np.array([
#     [120, 45, 88, 12],
#     [5, 99, 102, 0],
#     [400, 300, 250, 180],
#     [15, 22, 19, 31],
#     [88, 76, 92, 105]
# ])


# #Solution
# print(np.mean(inventory,axis=0))
# print(np.sum(inventory,axis=1))







# #Ticket 2: The AI Feature Scaler (Broadcasting + Axis)
# The Scenario:
# You are building a data pipeline for a Machine Learning model in a hospital.
# You have biometric data for 6 patients across 3 medical tests (Heart Rate, Blood Pressure, Sugar Level).
#     AI models cannot process raw data; the data must be "mean-centered."


# Your Business Requirements:

# Calculate the exact mean (average) for each of the 3 medical tests.

# Using vectorized broadcasting, subtract that array of 3 averages from the original biometrics matrix.

# Print the final (6, 3) normalized matrix. (If you use the wrong axis, NumPy will throw a shape mismatch error and crash).



# Rows: 6 Patients
# Columns: 3 Medical Tests
biometrics = np.array([
    [72, 120, 95],
    [85, 140, 105],
    [60, 110, 88],
    [92, 155, 112],
    [78, 125, 98],
    [88, 135, 101]
])

avg=np.mean(biometrics,axis=0)
b=biometrics-avg

print(avg)
print(b)
print(biometrics)