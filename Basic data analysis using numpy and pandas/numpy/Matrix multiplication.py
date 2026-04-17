import numpy as np

# a=np.array([
#     [2,4],
#     [8,3]
# ])


# b=np.array([
#     [2,4],
#     [4,3]
# ])

# c=np.array([
#     [2,3],
#     [4,2]
# ])

# print(a*b*c)   #matrices should be of same shape. multiplies corresponding elements








#---------------------------------------------- gemini ------------------------------------------------


# #Ticket 1: The Commutative Trap (Dimensional Geometry)The Scenario:You are mapping user coordinates to a new spatial grid. You are handed two matrices of the exact same shape.
# # Pythonimport numpy as np

# # # Shape: (4, 3)
# # matrix_A = np.array([
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9],
# #     [10, 11, 12]
# # ])

# # # Shape: (4, 3)
# # matrix_B = np.array([
# #     [0, 1, 0],
# #     [1, 0, 1],
# #     [0, 0, 1],
# #     [1, 1, 0]
# # ])
# # Your Business Requirement:If you try to compute matrix_A @ matrix_B, the engine will violently crash because the inner dimensions (3 and 4) do not match
# # .You must mathematically alter the physical geometry of matrix_B on the fly, and then perform the matrix multiplication so that the final output is a completely valid 4 x 4 matrix.
# # Print the resulting matrix





# matrix_A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ])

# # Shape: (4, 3)
# matrix_B = np.array([
#     [0, 1, 0],
#     [1, 0, 1],
#     [0, 0, 1],
#     [1, 1, 0]
# ])

# trans_b=np.transpose(matrix_B)

# print(matrix_A@trans_b)








#The Final Ticket: The Neural Network Forward Pass
# The Scenario:
# You are hard-coding the forward pass of an AI pipeline. You have a single input vector of data, a hidden layer of neural weights, and an output layer of neural weights.
# The data must flow sequentially from the input, through the hidden layer, and finally out through the output layer.



# # Input Data: Shape (1, 4)
# X = np.array([[0.5, 0.8, 0.2, 0.1]])

# # Hidden Layer Weights: Shape (4, 5)
# W1 = np.array([
#     [0.1, 0.2, 0.3, 0.4, 0.5],
#     [0.5, 0.4, 0.3, 0.2, 0.1],
#     [0.1, 0.1, 0.1, 0.1, 0.1],
#     [0.9, 0.8, 0.7, 0.6, 0.5]
# ])

# # Output Layer Weights: Shape (5, 2)
# W2 = np.array([
#     [0.1, 0.9],
#     [0.2, 0.8],
#     [0.3, 0.7],
#     [0.4, 0.6],
#     [0.5, 0.5]
# ])
# Your Business Requirement:
# Compute the sequential matrix multiplication.

# The Input must be multiplied by the Hidden Layer.

# That exact result must immediately be multiplied by the Output Layer.

# Print the final resulting matrix and its .shape attribute.






# Input Data: Shape (1, 4)
# X = np.array([[0.5, 0.8, 0.2, 0.1]])

# # Hidden Layer Weights: Shape (4, 5)
# W1 = np.array([
#     [0.1, 0.2, 0.3, 0.4, 0.5],
#     [0.5, 0.4, 0.3, 0.2, 0.1],
#     [0.1, 0.1, 0.1, 0.1, 0.1],
#     [0.9, 0.8, 0.7, 0.6, 0.5]
# ])

# # Output Layer Weights: Shape (5, 2)
# W2 = np.array([
#     [0.1, 0.9],
#     [0.2, 0.8],
#     [0.3, 0.7],
#     [0.4, 0.6],
#     [0.5, 0.5]
# ])


# step_1=X@W1
# step_2=step_1@W2
# print(step_2)
# print(np.shape(step_2))
