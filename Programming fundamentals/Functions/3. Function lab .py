# # # # # # #Write square(x) that returns x*x. Test with 12.

# # # # # # def square_fun(x:int) -> int:
# # # # # #     return x*x

# # # # # # square=square_fun(2)
# # # # # # print(square)






# # # # # #Write max_of_two(a,b) without using max(). Test (5,9) and (10,2).

# # # # # # def max_of_two(a,b):
# # # # # #     if a>=b:
# # # # # #         return a
# # # # # #     else:
# # # # # #         return b
    
# # # # # # print(max_of_two(2,3))






# # # # # # #Write min_of_two(a,b) without using min(). Test (5,9) and (10,2).

# # # # # # def min_of_two(a,b):
# # # # # #     return a if a<=b else b
# # # # # # print(min_of_two(2,3))




# # # # # #Write area_circle(r) that returns area = pi*r*r using math.pi. Test r=3.
# # # # # import math
# # # # # def area_circle(r):
# # # # #     return math.pi*r*r

# # # # # print(area_circle(2))






# # # # # #Return last character of string s (assume non-empty). Test "Python".

# # # # # def last_char(n:str)->str:
# # # # #     return n[-1]

# # # # # print(last_char("abuzar"))






# # # # # #Return 1 if n>0, 0 if n==0, -1 if n<0. Test -5, 0, 9.

# # # # # def test(n:int) -> int:
# # # # #     if n>0:
# # # # #         return






# # # # #----------Medium difficulty-----------


# # # # #Return sum 1..n using a loop. Assume n>=1. Test n=10.


# # # # # def sum_of_num(n:int) ->str:
# # # # #     total=0
# # # # #     for i in range(1,n+1):
# # # # #         total+=i

# # # # #     return f"Sum of (1-{n} is {total})"

# # # # # sum_n=sum_of_num(10)

# # # # # print(sum_n)







# # # # #Return n! for n>=0. If n<0 return None. Test 5,0,-2.

# # # # # def factorial(n:int) ->str:
# # # # #     if n<0:
# # # # #         return None
    
# # # # #     total=1
# # # # #     while n>0:
# # # # #         total*=n
# # # # #         n-=1
# # # # #     return f"factorial is {total}"

# # # # # print(factorial(5))
# # # # # print(factorial(0))
# # # # # print(factorial(-2))
    






# # # # # Return number of digits in positive integer n using while. Test 4725.

# # # # # def no_of_dig(n: int) -> int: # Promise an int
# # # # #     count = 0
# # # # #     while n > 0:
# # # # #         n //= 10
# # # # #         count += 1
# # # # #     return count # Deliver an int

# # # # # # The Terminal handles the human formatting
# # # # # test_num = 4725
# # # # # total_digits = no_of_dig(test_num)
# # # # # print(f"Total no of digits in {test_num} are {total_digits}")








# # # # # #Return sum of digits of positive integer n. Test 472 -> 13.

# # # # # def sum_of_int(n:int) ->int:
# # # # #     total=0
# # # # #     while n>0:
# # # # #         last_dig=n%10
# # # # #         total+=last_dig
# # # # #         n//=10

# # # # #     return total

# # # # # #Human terminal

# # # # # digit=1234
# # # # # sum_of_digits=sum_of_int(digit)
# # # # # print(f"Sum of {digit} is {sum_of_digits}")







# # # # # #Return reverse of positive integer n (e.g., 1204 -> 4021). Test 1204.


# # # # # def reve(n:int) ->int:
# # # # #     reve=0
# # # # #     while n>0:
# # # # #         last_dig=n%10
# # # # #         reve=reve*10+last_dig
# # # # #         n//=10
# # # # #     return reve

# # # # # #Human terminal

# # # # # digit=1204
# # # # # # reverse=reve(digit)
# # # # # # print(f"Reverse of {digit} is {reverse}")








# # # # # #Return True if n is prime else False. Use loop. Test 1,2,9,13.

# # # # # # def check(n:int) ->int:
# # # # # #       if n<2:
# # # # # #             return False
    
# # # # # #       for d in range(2,n):
# # # # # #                   if n%d==0:
# # # # # #                         return False
                  
# # # # # #       return True
                  
# # # # # # print(check(1))
# # # # # # print(check(2))
# # # # # # print(check(9))
# # # # # # print(check(13))









# # # # # # #Return reverse of s without slicing. Test "python".

# # # # # # def reverse_str(n:str) -> str:
# # # # # #     rev=""
# # # # # #     i=len(n)-1
# # # # # #     while i>=0:
# # # # # #             rev+=n[i]
# # # # # #             i-=1
        
# # # # # #     return rev

# # # # # # print(reverse_str("python"))








# # # # # #Return number of words in sentence using split(). Test "We love Python".

# # # # # def words_count(n:str)-> str:
# # # # #     words=n.split()
# # # # #     return len(words)

# # # # # #Frontend

# # # # # sentence="we love python"
# # # # # no_of_words=words_count(sentence)
# # # # # print(no_of_words)







# # # # #Return maximum value without using max(). Assume non-empty list. Test [3,9,2,11,5] -> 11.

# # # # def maximum(nums:list):
# # # #     maximum_value=nums[0]
# # # #     for i in nums[1:]:
# # # #         if i > maximum_value:
# # # #             maximum_value=i

# # # #     return maximum_value

# # # # #Front end
# # # # nums=[3,9,2,11,5]
# # # # maximum_list_value=maximum(nums)
# # # # print(maximum_list_value)







# # # #Convert s to float. If fails return None. Test "3.14", "12", "abc".
# # # def conversion(string:str):
# # #     try:
# # #         x=float(string)
# # #         return x
# # #     except:
# # #         None

# # # print(conversion("3.14"))
# # # print(conversion("12"))
# # # print(conversion("abc"))






# # # #Return length of string without len(). Test "Hello world".

# # # def len_str(n:str):
# # #     lenght=0
# # #     for i in n:
# # #         lenght+=1
# # #     return lenght

# # # string="Hello world"
# # # len_of_str=len_str(string)
# # # print(len_of_str)







# # #Return "Last, First" with capitalization. Test ("aLI","kHaN") -> "Khan, Ali".

# # def cap(n1:str,n2:str):
# #     return f"{n1.capitalize()} and {n2.capitalize()}"

# # print(cap("aLI","kHaN"))






# #random password generator

# import string 
# import random

# def pass_gen(lenght:int) -> str:
#     password=""
#     a=string.ascii_letters+string.digits+string.punctuation
#     for i in range(lenght):
#             g=random.choice(a)
#             password+=g

#     return f"Random password of lenght {lenght} is {password}"

# #Human terminal
# password_lenght=10
# random_password=pass_gen(password_lenght)
# print(random_password)








# # # # #Return sum of two same-size 2D lists. Test A=[[1,2],[3,4]] and B=[[10,20],[30,40]].

# def sum_list(a:list,b:list)->list:
#     outer_list=[]
#     for i in range(2):
#         inner_list=[]
#         for j in range(2):
#             inner_list.append(a[i][j]+b[i][j])
#         outer_list.append(inner_list)
        
#     return outer_list

# print(sum_list([[1,2],[3,4]],[[10,20],[30,40]]))







# # #Return True iff length>=8, has at least one digit, and has at least one uppercase. Test: "abc",
# # # "abcdEFGH", "abcdEFG1".

# import string
# def validate(a:str)->bool:
#     if len(a)<8:
#         return False
    
#     has_digit=False
#     has_upper=False
#     for char in a:
#         if char.isdigit():
#             has_digit=True

#         if char.isupper():
#             has_upper=True
        
#         if has_digit and has_upper:
#              break

#     return has_upper and has_digit

# print(validate("abcdefghijkl"))
        


   
# # print(validate("1ba"))








