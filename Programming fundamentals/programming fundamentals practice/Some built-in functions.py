# # a=float(input("Enter 1st digit:"))
# # b=float(input("Enter 2nd digit:"))
# # c=float(input("Enter 3rd digit:"))




# # print(max(a,b,c))

# # print(min(a,b,c))



# a=float(input("Enter 1st digit:"))
# b=float(input("Enter 2nd digit:"))
# c=a/b

# print(round(c,2))    #round(value,no of digits round off)


# # a=float(input("Enter 1st digit:"))
# # b=float(input("Enter 2nd digit:"))


# # print(abs(a))



# #Check if specific element is in str , tup , list etc
# b="apple"

# print("Z" in b)



# #Title (It takes 1st letter of string as upper case and rest lower case)


# # x=input("Enter a word:").title()  #It will capatalize the 1st character of every word
# # y=input("Enter a sentence:").title() #It will capatalize the 1st character of every word in then sentence


# # print(x)
# # print(y)



# #Upper and Lower

# # w=input("Enter in upper case:").lower()   #Converts all words in lower case
# # q=input("Enter in lower case").upper()   #Converts all words in upper case

# # print(w)
# # print(q)



# #Count (It couts specific elements in a str)

# r=("12433934898789789789734897298379789797818743874287")
# print(r.count("2"))



# z="Hello.Hello.Hello.Hello.Hello.Hello"

# print(z.count("Hello")) #6


# #We can mention index values in which we can search

# v="aaaaaaaaaaabbbbbbbbbbbaaaaaaaaaaaabababababbabababzzzzzzzzxvbjhgdeuydeyu"

# print(v.count("z",10,len(v)))    #count("Word to count",starting index,ending index)


#.strip()
# i removes unwanted spaces at start or end of of string we can also use lstrip or rstrip . (left and right)

name=input("Enter your name:").strip("#").lower() #we can use anything to be removed, in strip 
print(name)