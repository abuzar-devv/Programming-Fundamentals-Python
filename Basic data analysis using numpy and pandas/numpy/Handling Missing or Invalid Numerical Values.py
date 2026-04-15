import numpy as np

#--------------------------------Gemini-------------------------------------


# #Ticket 1: The Sensor Imputation (Column-Wise Rescue)
# The Scenario:
# You are receiving data from 3 temperature sensors over 5 hours. Due to network packet loss, several readings are missing and have registered as NaN. You cannot train an AI model on data containing NaNs
# but you also cannot afford to delete the rows.

# Python
# import numpy as np

# # Shape: (5, 3)
# sensor_data = np.array([
#     [12.5, np.nan, 45.2],
#     [10.1, 22.3, np.nan],
#     [np.nan, 21.0, 44.8],
#     [11.2, 23.1, 46.5],
#     [14.0, np.nan, np.nan]
# ])
# Your Business Requirement:
# You must perform "Mean Imputation". Calculate the safe mean of each of the 3 columns (ignoring the missing values).
# Then, locate every single NaN in the matrix and overwrite it with the exact mean of its respective column.
# Print the final, fully restored (5, 3) matrix.






# # Shape: (5, 3)
# sensor_data = np.array([

#     [12.5, np.nan, 45.2],
#     [10.1, 22.3, np.nan],
#     [np.nan, 21.0, 44.8],
#     [11.2, 23.1, 46.5],
#     [14.0, np.nan, np.nan]

# ])

# avg=np.nanmean(sensor_data[:,-1:])
# print(f"Avg is {avg}")
# sensor_data[np.isnan(sensor_data)]=avg
# print(sensor_data)









#Ticket 2: The Corrupted Batch (Threshold Filtering)
# The Scenario:
# You are processing a database of user profiles. Each row is a user, and each column is an attribute. Some users abandoned their sign-up process halfway through,
# leaving massive holes in the dataset.

# Python
# # Shape: (6, 4)
user_profiles = np.array([
    [25.0, 60000.0, np.nan, 85.0],
    [np.nan, np.nan, 5.0, 92.0],
    [45.0, 120000.0, 10.0, np.nan],
    [np.nan, np.nan, np.nan, np.nan],
    [30.0, 85000.0, 3.0, 78.0],
    [28.0, np.nan, 1.0, 90.0]
])
# Your Business Requirement:
# If a user is missing data, that is fine. But if a user is missing 2 or more attributes, their profile is completely useless to the business.
# You must calculate how many NaNs exist in each individual row. If a row contains 2 or more NaNs, you must completely delete that row from the matrix.
# Print the final cleaned matrix.



np.set_printoptions(suppress=True)   # do not want scientiic notation

user_profiles = np.array([
    [25.0, 60000.0, np.nan, 85.0],
    [np.nan, np.nan, 5.0, 92.0],
    [45.0, 120000.0, 10.0, np.nan],
    [np.nan, np.nan, np.nan, np.nan],
    [30.0, 85000.0, 3.0, 78.0],
    [28.0, np.nan, 1.0, 90.0]
])
user_profiles[np.isnan(user_profiles)]=0
print(user_profiles)


# data=np.array([1,2,3,4,np.nan])
# print(np.isnan(user_profiles))

# print(np.nanmean(data))
# print(np.nanmax(data))