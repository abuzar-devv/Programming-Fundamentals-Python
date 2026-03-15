# x=input("Enter your name:")
# y=input("Enter your system name:")
# print(f"Hello! welcome back {x} your system name is {y} good luck with it")



# for i in range (1,6):
#     x=float(input("Enter 1st digit:"))
#     y=float(input("Enter 2nd digit:"))
#     z=x+y

#     print(f"Answer of calculation no {i} is {z} ")

try:
    print("Welcome to driving liscence management system")
    for i in range(1,6):

       
        age=int(input("Enter your age:"))

        if age >=18:
            name=input("Enter your name:")
            print(f"{name} your age is {age} , so you can get a driving liscence! Gadi sai chalaen!")

        else:
            name=input("Enter name:")
            print(f"{name} tainaiya aram nal beya halay tu {age} saal da aen!")

except Exception as e:
    print(e)



    