#While loop
# i=0
# while i<=5:
#     print("Hello")
#     i+=1

#Table of 2 (till 100)

# num=0  #num is iterator 
# while num<=100:
#     print(num)
#     num+=2

#One complete loop is iteration

#Reverse

# i=10
# while i>=0:
#     print(i)
#     i-=1

#Table of n

# n=int(input("Enter a number to print its multiplication table:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
    
#commision calc

# try:
#     profit_list=[]
#     cond="y"

#     while cond=="y":
#         price_Wholesale=float(input("Enter the wholesale price of product: "))

#         retail_price=float(input("Enter the retail price of product: "))

#         n=int(input("Enter the number of products:"))

#         profit=(n*retail_price)-(n*price_Wholesale)

#         print("profit:",profit)
        
#         add_to_list=input("Enter yes to add profit to final profit list:").lower()

#         if add_to_list=="yes":
        
#             profit_list.append(profit)

#         else:
#             print("Not added")


#         cond=input("Enter y to run loop again or enter anything to print final profit list:").lower()


#     print(profit_list)

# except Exception as e:
#     print(e)


# nums=[44,33,22,11,55,66,77,23,45,21]

# n1=int(input("Enter starting index value:"))
# n2=int(input("Enter stoping index value:"))

# while (n1>=0 and n1<len(nums)) and (n2>n1 and n2<len(nums)):
#     print(nums[n1:n2])
#     n2+=1



# x=[98,33,44,2,1,3,4]
# n=int(input("Enter starting index value:"))
# while n<len(x):
#     print(x[n])
#     n+=1



# x=(99,11,22,33,4,5,6,)
# i=0

# while i<len(x):
#     if (x[i]==33):
#         print("33 found at idx:",i)
#     else:
#         print("not found!")

#     i+=1



# tup=(99,22,11,44,55,66,77,88,123)
# n=int(input("Enter starting index: "))

# while n<len(tup):
#     if (tup[n]==77):
#         print("Found",n)
#         break
#     else:
#         print('not found')
#     n+=1
# print("End")



# i=0
# while i<=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1


# max_temperature=50

# temperature=float(input("Enter current temp in celcius:"))

# while temperature>=max_temperature:
#     print("Its too hot decrease the temperature!")

#     temperature=float(input("Enter current temp in celcius:"))

# print("Temperture is good now!")


# #For loop
# veg=["potato","carrot"]
# for val in veg:
#     print(val)



# total = 0

# # range(1, 11) gives i the values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# for i in range(1, 11):
#     # Take the current total and add the value of 'i'
#     total = total + i 
#     print("Added", i, "to get a total of", total)

# print("The final summation is:", total)



# print (" This program prints numbers and their squares .") # Explain
# end = int ( input (" How high should I go? ") ) # User

# print (" Number \ t Square ") # Header
# print (" --------------")
# for number in range (1 , end + 1) : # end +1 to

#     square = number ** 2 # Square
#     print ( number , "\t" , square )


#sum of 1st 20 digits
# total=0

# for i in range(20):
#     total=total+i
#     print("added ",i,"to get total of :",total)
    
# print("final total:",total)


MAX = 5 # Number of values
total = 0 # Accumulator
for _ in range ( MAX ) : # Iterate MAX times
    n = int ( input (" Enter a number : ") ) # Read integer
    total = total + n
    print (" Total :", total )


















