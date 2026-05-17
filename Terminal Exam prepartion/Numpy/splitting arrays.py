import numpy as np

matrix = np.array([

    [12, 45, 78, 3, 66, 90, 21, 54],
    [33, 10, 88, 71, 29, 40, 63, 57],
    [95, 18, 27, 64, 6, 49, 82, 11],
    [74, 39, 55, 13, 92, 8, 30, 61],
    [26, 84, 17, 50, 73, 41, 69, 4],
    [58, 22, 97, 35, 14, 80, 46, 68]

])

# print(matrix)
# print(np.hsplit(matrix,2))
print(np.split(matrix,3,axis=0))
print(np.split(matrix,2,axis=0))

print(np.split(matrix,2,axis=1))
print(np.split(matrix,4,axis=1))

