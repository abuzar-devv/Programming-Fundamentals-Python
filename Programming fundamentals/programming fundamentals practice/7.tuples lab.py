# # #Given p=(3,7,9), unpack into x,y,z and print x+y+z.

# # # p=(3,7,9)
# # # x,y,z=p
# # # print(x+y+z)







# # # #Given t=(1,2,3,2,1), print True if palindrome else False.
# # # t=(1,2,3,2,1)

# # # if t[0:]==t[::-1]:
# # #     print("True")

# # # else:
# # #     print("False")






# # #Given a tuple t, print True if it is sorted ascending, else False. Test with t=(1,3,4,9,10).
# # t=(1,3,4,9,10,11)
# # status=True

# # for i in range(1,len(t)):
# #     if t[i]<t[i-1]:
# #         status=False
# #         break

# # print(status)







# #Given t=(1,2,3,4,5,6), create (2,1,4,3,6,5).

# # t=(1,2,3,4,5,6)
# # new=[]                                    # insert(index,value)

# # for i in range(0,len(t),2):
# #     new.append(t[i+1])
# #     new.append(t[i])

# # print(tuple(new))







# # #Input n and build a tuple (1,4,9,...,n^2) using a loop.

# # n=int(input("Enter ending value:"))
# # t=[]

# # for i in range(1,n+1):
# #     t.append(i**2)

# # print(tuple(t))







# #Given t=(4,1,4,2,1,3,2,4), create (4,1,2,3).

# # tup=(4,1,4,2,1,3,2,4)
# # t=[]

# # for i in tup:
# #     if i not in t:
# #         t.append(i)

# # print(tuple(t))






# #Create a list: [("Ali",80),("Sara",92),("Omar",75)] and print each record.

# # info=[("Ali",80),("Sara",92),("Omar",75)]


# # for name , score in info:
# #     print(f"{name} = {score}")








# # #Given students=[("Ali",80),("Sara",92),("Omar",75)], sort by marks ascending.

# # students=[("Ali",80),("Sara",92),("Omar",75)]
# # result=[]


# # for name , marks in students:
# #     result.append((marks,name))

# # result.sort()

# # print(result)






# # #Alternate


# # students = [("Ali", 80), ("Sara", 92), ("Omar", 75)]

# # students.sort(key=lambda x: x[1])

# # print(students)










# #Given a=[3,9,2,9,5], find (max_value, index) using a loop.

# # a=[3,9,2,9,5]
# # max_val=a[0]
# # index=0

# # for i in range(len(a)):
# #     if a[i]>max_val:
# #         max_val=a[i]
# #         index=i

# # print(f"{max_val} is at index : {index}")








# #Given a=(1,2,3) and b=("x","y","z"), build a list of pairs and print it.

# a=(1,2,3)
# b=("x","y","z")

# for num,var in zip(a,b):
#     print(num,var)






# #Given t=("Ali","Sara","Omar"), print index and name using unpacking.

# t=("Ali","Sara","Omar")

# for i , name in enumerate(t):
#     print(i,name)








