import numpy as np

# print(np.zeros(5))




#Print the element 6, the first row, the last row, and the second column.


# matrix=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(matrix[1:2,-1:])
# print(matrix[0])
# print(matrix[-1])
# print(matrix[0:,1])










#Create an array from 1 to 12. Then reshape it into:
# a 3 by 4 matrix
# a 2 by 6 matrix
# Print the shape of both matrices.

# matrix=np.arange(1,13)
# print(matrix.reshape(3,4))
# print(matrix.reshape(2,6))








#Create a 3 by 3 matrix using numbers 1 to 9. Find:
# sum of all values
# sum of each row
# sum of each column


# matrix=np.arange(0,9).reshape(3,3)
# print(np.sum(matrix))
# print(np.sum(matrix,axis=1))
# print(np.sum(matrix,axis=0))








#Prices are [100, 250, 500, 750]. Add 10% sales tax to every price. Then apply a discount of 50 to every taxed price

# prices=np.array([100, 250, 500, 750])
# sales_tax=prices*1.10
# discount=sales_tax-50
# print(sales_tax)
# print(discount)






import random

# #Generate a 4 by 4 matrix of random integers from 1 to 20. Print:
# # the matrix
# # maximum value in each row
# # minimum value in each column
# # Use a random seed so the output is repeatable.
# np.random.seed(10)
# matrix=np.random.randint(1,21,size=(4,4))
# print(matrix)
# print(np.max(matrix,axis=1))
# print(np.min(matrix,axis=0))








# #Temperatures in Celsius are [0, 10, 20, 30, 40]. Convert them to Fahrenheit using:
# F = C × (9/5)+32

# Print both arrays.

# C=np.array([0, 10, 20, 30, 40])
# F=C * (9/5)+32
# print(F,C)








# #Use marks [35, 48, 50, 72, 91, 29]. Create a new array where:
# # marks below 50 become 0
# # marks 50 or above remain unchanged


# marks=np.array([35, 48, 50, 72, 91, 29])
# new_marks=np.where(marks<50,0,marks)
# print(new_marks)








# #Three students have marks in three subjects:

# Find each student’s total and average marks.



marks=np.array([
    [80,75,90],
    [60,65,70],
    [95,85,88]

])



print(f"Total marks of each student = {np.sum(marks,axis=1)}")
print(f"Average marks of each student = {np.mean(marks,axis=1)}")
