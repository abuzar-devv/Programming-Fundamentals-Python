# # a = [1 , 2 , 3]
# # b = [4 , 5 , 6]
# # c = a + b
# # print ( c ) # List concatination



# #Copy 


# # a=[1,2,3]
# # b=a.copy()
# # print(a,b)



# #Replacing elements

# # elemnts=[1,2,3,4,5]
# # elemnts[0:len(elemnts)-2]=["a","b","c"]
# # print(elemnts)


# #Extend()

# # a=[1,2,3]
# # b=[4,5,6]
# # a.extend(b)
# # print(a)



# # Sort() it arranges in assending order by default

# # a=[2,1,99,88,33]
# # a.sort()
# # print(a)


# # Descending sort

# # a=[0,88,1,44,99]
# # a.sort(reverse=True)
# # print(a)



# # pop(index value) it removes by index values. as default pop() removes last index value it also returns 

# # a=[3,4,5]
# # x=a.pop()
# # print(x)
# # print(a)


# # del()  can remove multiple index values using slicing and oit returns nothimng


# # a=[0,1,2,3,4,5,6,7,9]
# # del a[0:4]
# # print(a)



# # Remove()  it removes 1st occurance of required element


# # a=[2,4,5,6,2]
# # x=a.remove(2)
# # print(x) #Returns nothing
# # print(a)



# #String to list 


# # a="aeiou"
# # print(list(a)) #type casting



# #Split () converts into list of words while () act as a cutting point for splitting


# # a="ABCXDEFGHIXKL"
# # d="i love python"
# # b=a.split("X") #Acted as a cutting point for splitting
# # c=d.split() #default
# # print(b,c)




# #Join() is reverse of split()  works only on str

# # a=["i","love","python"]
# # b=" ".join(a)   #While " ".join() the lefty part is what to add between words
# # print(b)


# # c=["i","am","abuzar"]
# # d="-".join(c)
# # print(d)




# # use of == and is

# # is is used Are they literally the same thing in memory

# a=[1,2,3]
# b=[1,2,3]
# print(a==b) #check if both have same value
# print(a is b) #Both are different in memory


# #str
# a="Hello"
# b="Hello"

# print(a is b) #May be true depending upon python optimization

# #Sometimes Python stores the same value in one memory location and makes multiple variables point to it.

# # So is (which checks memory) may give:

# # True → same memory used
# # False → different memory created




# #Alising

# a=[1,2,3]
# b=a
# b[0]="a"
# print(a,b)  #both lists show the same result because a and b refer to the same list object in memory (aliasing), so changes through one affect the other









