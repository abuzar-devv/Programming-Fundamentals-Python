import numpy as np
import random

np.random.seed(9)

a=np.random.rand(5)    # Gives random values between 0 and 1
print(a)


b=np.random.randint(0,100,1) # ------> (start,stop,number of random value)
print(b)

c=np.random.randn(10)
print(c)