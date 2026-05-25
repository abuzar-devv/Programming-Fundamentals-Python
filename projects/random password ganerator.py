#random password generator

import string 
import random

def pass_gen(lenght:int) -> str:
    password=""
    a=string.ascii_letters+string.digits+string.punctuation
    for i in range(lenght):
            g=random.choice(a)
            password+=g

    return f"Random password of lenght {lenght} is {password}"

#Human terminal
password_lenght=50
random_password=pass_gen(password_lenght)
print(random_password)