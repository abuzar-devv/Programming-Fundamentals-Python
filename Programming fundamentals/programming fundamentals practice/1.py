# #check even odd

# number=int(input("Enter a digit:"))


# if number%2==0:
#     print("Even")
# else:
#     print("Odd")



#6. Write a program that checks whether a number is divisible by both 3 and 5.

# number=int(input("Enter a digit:"))

# if (number%3==0) and (number%5==0):
#     print("Divisible!")
# else:
#     print("not divisible!")


#7. Write a program that checks whether a number is divisible by 3 or 7


# number=int(input("Enter a digit:"))

# if (number%3==0) or (number%7==0):
#     print("Divisible!")
# else:
#     print("not divisible!")



#8. Write a program that checks whether a number is NOT negative.

# num=float(input("Enter a digit:"))

# if num >=0 :
#     print("Not -ve")
# else:
#     ("Negative")


#13. a simple login program that checks username = 'admin' and password = '1234'


# username=input("Enter username:")
# password=input('Enter password:')

# if (password=='1234')  and  (username=='admin'):
#     print("Login successful!")

# else:
#     print("login denied!")


#14. Write a program to check whether a given number is integer or float.


# num=float(input("Enter a digit:"))

# if num.is_integer():
#     print("Integer!")
# else:
#     print("Float")



#Write a program that converts a user input into int, float, and string and prints
# their types


# a=input("enter:")
# b=int(input("Enter:"))
# c=float(input("Enter:"))


# print(type(a))

# print(type(b))

# print(type(c))


#Write a program to determine whether a year is a leap year.
#take days input



# Write a program to determine the largest among three numbers.


a=float(input("enter:"))
b=float(input("enter:"))
c=float(input("enter:"))


if a>=b and a>=c:
    print(a, "is largest")

elif b>=a and b>=c:
    print(b, "is largest")

else:
    print(c, 'is largest')


