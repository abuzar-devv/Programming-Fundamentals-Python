# # # #Given a = [1, 2, 3] and b = [4, 5], extend a with b, then print a.
# # # a=[1,2,3]
# # # b=[4,5]
# # # a.extend(b)
# # # print(a)





# # #Read 5 names into a list, then print each name with its index like: 0: Ali, 1: Sara, ...

# # # names=["ali","abuzar","hamza","ahmad","moiz"]
# # # index=0

# # # for name in names:
# # #     print(f"{index}:{name}")
# # #     index+=1





# # #Given letters = [’P’,’A’,’K’,’I’,’S’,’T’,’A’,’N’], join them into a single string
# # "PAK" and print

# # letters = ["p","a","k","i","s","t","a","n"] 
# # word = "". join ( letters ) # join with empty delimiter
# # print ( word )
           




# # #Read 7 integers into a list and count how many are exactly 0. Print the count.

# # num=[]
# # count=0

# # for i in range(7):
# #     n=int(input("Enter integer:"))
# #     num.append(n)

# #     while n>0:
# #         last_dig=n%10
# #         if last_dig==0:
# #             count+=1
# #         n//=10

# # print(f"There are {count} zero in {num}")







# #Read 8 integers into a list. Replace any negative value with 0. Print the updated list.

# # num=[]

# # for i in range(8):
# #     n=int(input("Enter integer:"))
# #     num.append(n)

# #     if n<0:
# #         num[i]=0

# # print(num)







# #Given p = [9, 8, 7, 6, 5], swap the first and last elements.

# # p = [9, 8, 7, 6, 5]

# # p[0]=5
# # p[-1]=9
# # print(p)






# #Given v = [1,2,3,4,5,6,7,8], replace the middle four elements with [99,100].

# v = [1,2,3,4,5,6,7,8]

# v[0:4]=[99,100]
# print(v)






# #Given x=[1,2,3,4], make a copy y. Change y[0] to 99. Print x and y.
# x=[1,2,3,4]

# y=x.copy()
# x[0]=99
# print(x,y)







#Given nums=[9,2,11,7,11,3], find the second largest distinct value using loops.
# 
# 
# 
#  also try smallest and 3 rd largest in similar logic
# nums = [9, 2, 11, 7, 11, 3]

# largest = float('-inf')
# second = float('-inf')

# for x in nums:
    
#     if x > largest:
#         second = largest
#         largest = x

#     elif x > second and x != largest:
#         second = x

# print(second)








#Given a=[10,20,30,40,50], rotate left by 1: result should be [20,30,40,50,10].\

a=[10,20,30,40,50]

print(a[1:] + [a[0]])