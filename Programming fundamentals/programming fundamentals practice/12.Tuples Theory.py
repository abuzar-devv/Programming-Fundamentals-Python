# print(type(("A")))
# print(type(("A",)))  #Tuple cannot contain single elemet but only with (1,) extra coma that would create it a single element tuple






# #Type casting

# a="abuzar"
# b=[1,2,3,4]

# print(tuple(a))

# print(tuple(b))






# #Nested tuples

# a=(
#     (1,2),
#     (3,4),
#     (5,6)

# )






#Membership

# num=(2,3,4,5,6,7)
# print(100 in num) #False








# #Safe replacement in tuples by slicing and concatination


# # a=("a","b")
# # b=(1,2)
# # print(a+b)


# # name=("b","u","z","a","r")
# # print(("a",) + name[0:])





# #Packing
# # a="ali",1,True    #Tuple
# # print(type(a))




# # #Un-Packing

# # a=(1,2)
# # x,y=a
# # print(x,y,a)








# #Swapping values in tuples

# # a=5
# # b=7

# # a,b=b,a

# # print(a,b)






# #DSU

# # text="I love python programming"
# # words=text.split()
# # decortaed=[]

# # for word in words:
# #     decortaed.append((len(word),word))

# # decortaed.sort(reverse=True)

# # results=[]

# # for len,w in decortaed:
# #     results.append(w)

# # print(results)







# #modern way of dsu 


# text = "I love python programming"
# words = text.split()

# results = sorted(words, key=len, reverse=True)

# print(results)








# eunamarate() , dict.items() , zip()


# a=(8,3,2,1,4)

# for i , val in enumerate(a):
#     print(i,val)



# b={"a":9,"b":"abuzar"}

# for key , val in dict.items(b):
#     print(key,val)




a=(12,13,20,16)
b=(22,33,44,)

for age, marks in zip(a,b):
    print(age,marks)