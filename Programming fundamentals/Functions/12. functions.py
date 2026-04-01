# print(max("apple","Cherry","banana"))
# print(min("apple","Cherry","banana"))

#-------👉 Strings are compared letter by letter from left; the first different letter decides, and if all letters match, the shorter word is smaller.----------


import math
 
# x=math.sqrt(4)
# print(x)

# radians=0.5
# print(math.sin(radians))


# degree=86
# degree_to_rad=math.radians(degree)
# print(math.sin(degree_to_rad))




import random

# # random.seed(5)
# # print(random.randint(1,100))

# x=[1,2]

# print(random.choice(x))





#generating 10 different randoms
import random

def rand(num):
    for i in range(num):
        random.seed(0)
    
        x=random.randint(1,1000)
        print(x)


rand(10)







#------Nested calls-------

# #One function can call another:
# main() calls A()
# A() calls B()
# B() returns to A()
# A() returns to main()
# Python tracks where to return automatically.


