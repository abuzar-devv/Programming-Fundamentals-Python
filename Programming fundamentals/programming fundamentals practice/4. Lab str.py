# # # # # # # # # # # # # # # # # # #Input a string and print the index of the first occurrence of "e" using find().

# # # # # # # # # # # # # # # # # # sentence=input("Enter a sentence:")

# # # # # # # # # # # # # # # # # # print(sentence.find("e"))




# # # # # # # # # # # # # # # # # #Input a string of length at least 3. Print first 3 and last 3 characters using slicing.


# # # # # # # # # # # # # # # # # # sentence=input("Enter a sentence:")

# # # # # # # # # # # # # # # # # # print(f"First 3 char are {sentence[:3]} and last 3 char are {sentence[-3:]}")






# # # # # # # # # # # # # # # # # #Input a string and print its characters in reverse order, one per line.


# # # # # # # # # # # # # # # # # # sentence=input("Enter a sentence:")

# # # # # # # # # # # # # # # # # # for i in sentence[::-1]:
# # # # # # # # # # # # # # # # # #     print(i)





# # # # # # # # # # # # # # # # # # Input a string and build its reverse into a new string, then print it.

# # # # # # # # # # # # # # # # # # sentence=input("Enter a sentence:")

# # # # # # # # # # # # # # # # # # print(sentence[::-1])




# # # # # # # # # # # # # # # # # #Input a string and print True/False if "cat" is inside it using in.

# # # # # # # # # # # # # # # # # # sentence=input("Enter a sentence:")

# # # # # # # # # # # # # # # # # # print("cat" in sentence)








# # # # # # # # # # # # # # # # # #-------M sets----------


# # # # # # # # # # # # # # # # # # #Input a line and count words without using split(). Treat consecutive spaces as one separator.

# # # # # # # # # # # # # # # # # # line=input("Enter a line:")

# # # # # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # # # # in_word=False

# # # # # # # # # # # # # # # # # # for char in line:

# # # # # # # # # # # # # # # # # #     if char!=" " and not in_word:
# # # # # # # # # # # # # # # # # #         count+=1
# # # # # # # # # # # # # # # # # #         in_word=True

# # # # # # # # # # # # # # # # # #     elif char==" ":
# # # # # # # # # # # # # # # # # #         in_word=False   

# # # # # # # # # # # # # # # # # # print(f"Total words are {count}")









# # # # # # # # # # # # # # # # # #Input text. Count how many times "ana" occurs (overlaps allowed) without using count().

# # # # # # # # # # # # # # # # # # text=input("Enter text:").strip()
# # # # # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # # # # for i in range(len(text)):
# # # # # # # # # # # # # # # # # #     if text[i:i+3]=="ana":

# # # # # # # # # # # # # # # # # #         count+=1
        
# # # # # # # # # # # # # # # # # # print(f"Occurance of ana is {count}")






# # # # # # # # # # # # # # # # # # #Input a string and a character. Print all indices where the character occurs.
# # # # # # # # # # # # # # # # # # text=input("Enter:").lower()
# # # # # # # # # # # # # # # # # # char="a"
# # # # # # # # # # # # # # # # # # count=0

# # # # # # # # # # # # # # # # # # for i in range(len(text)):
# # # # # # # # # # # # # # # # # #     if text[i]==char:
# # # # # # # # # # # # # # # # # #         count+=1
# # # # # # # # # # # # # # # # # #         print(f"{char} is at index {i}")

# # # # # # # # # # # # # # # # # # print(f"Total occurance of {char} is {count}")







# # # # # # # # # # # # # # # # # #Input a string and check if it is a palindrome ignoring case (do not remove spaces). Print
# # # # # # # # # # # # # # # # # # True/False.


# # # # # # # # # # # # # # # # # text=input("Enter text to test palindrome:").lower()

# # # # # # # # # # # # # # # # # if text[0:] == text[::-1]:
# # # # # # # # # # # # # # # # #     print(True)

# # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # #     # print(False)










# # # # # # # # # # # # # # # # #Input an email like user@domain.com. Extract and print domain.com. (Assume exactly one ’@’.)
# # # # # # # # # # # # # # # # email=input("Enter your email:")
# # # # # # # # # # # # # # # # for i in range(len(email)):
# # # # # # # # # # # # # # # #     if email[i]=="@":
# # # # # # # # # # # # # # # #         print(email[i+1:])
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print("No domain")







# # # # # # # # # # # # # # # #Input a sentence and convert it to title case: first letter of each word uppercase, rest unchanged. (Words separated by spaces.)


# # # # # # # # # # # # # # # sentence=input("Enter sentence:")
# # # # # # # # # # # # # # # words=sentence.split()
# # # # # # # # # # # # # # # capatalized_sentence=""

# # # # # # # # # # # # # # # for word in words:
# # # # # # # # # # # # # # #     capatalized_sentence+=word.capitalize()+" "

# # # # # # # # # # # # # # # print(capatalized_sentence)









# # # # # # # # # # # # # # #Input a string and replace multiple consecutive spaces with a single space. (Example: "a b" -> "a b")

# # # # # # # # # # # # # # # text = input("Enter text: ")

# # # # # # # # # # # # # # # while "  " in text:
# # # # # # # # # # # # # # #     text = text.replace("  ", " ")

# # # # # # # # # # # # # # # print(text)











# # # # # # # # # # # # # # #Input a string and print True if it is a valid integer (optional leading + or -), else False. (No int() conversion for checking.)
# # # # # # # # # # # # # # text = input("Enter: ")

# # # # # # # # # # # # # # # Case 1: If number starts with + or -
# # # # # # # # # # # # # # if text.startswith("+") or text.startswith("-"):
# # # # # # # # # # # # # #     number_part = text[1:]  # remove the sign
# # # # # # # # # # # # # #     result = number_part.isdigit()

# # # # # # # # # # # # # # # Case 2: No sign at the start
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     result = text.isdigit()

# # # # # # # # # # # # # # print(result)
    










# # # # # # # # # # # # # #Input a string. Find the second occurrence of "na" using find() with a start index. Print the index (or -1 if not found)

# # # # # # # # # # # # # text = input("Enter:").lower()

# # # # # # # # # # # # # first = text.find("na")

# # # # # # # # # # # # # if first == -1:
# # # # # # # # # # # # #     print(-1)
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     second = text.find("na", first + 1)
# # # # # # # # # # # # #     print(second)









# # # # # # # # # # # # #Input two strings. Remove ’.’, ’,’, ’ !’, ’?’ from both (using replace) and compare ignoring case. Print Same or Different.

# # # # # # # # # # # # import string
# # # # # # # # # # # # str1=input("Enter str 1:")
# # # # # # # # # # # # str2=input("Enter str 2:")


# # # # # # # # # # # # for p in  string.punctuation:
# # # # # # # # # # # #     str1=str1.replace(p,"")
# # # # # # # # # # # #     str2=str2.replace(p,"")

# # # # # # # # # # # # if str1.lower()==str2.lower():
# # # # # # # # # # # #     print("Same")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("different")







# # # # # # # # # # # #Input a string that contains parentheses like: abc(def)ghi Extract and print the substring inside the first pair of parentheses.

# # # # # # # # # # # text=input("Enter:")

# # # # # # # # # # # for i in range(len(text)):
# # # # # # # # # # #     if text[i]=="(":
# # # # # # # # # # #         n1=i
# # # # # # # # # # #         break

# # # # # # # # # # # for i in range(len(text)):  #in 2nd place of range its -1 because ending index is not counted so 0 will be consoidered
# # # # # # # # # # #     if text[i]==")" and i>n1:
# # # # # # # # # # #         n2=i
# # # # # # # # # # #         break

# # # # # # # # # # # print(f"Substring in middle of () is {text[n1+1:n2]}")








# # # # # # # # # # #Input a string and print counts of a,e,i,o,u (case-insensitive). No lists/dicts.


# # # # # # # # # # sentence=input("Enter text for vowel count:").lower()
# # # # # # # # # # vowels="aeiou"

# # # # # # # # # # for vowel in vowels:
# # # # # # # # # #     count=0
# # # # # # # # # #     for i in sentence:
# # # # # # # # # #         if i==vowel:
# # # # # # # # # #             count+=1

# # # # # # # # # #     print(f"{vowel} occurs in {sentence} : {count} times")









#Input a full name like "Ali Raza Khan" and print initials like A.R.K (Assume words separated by single spaces; name starts with a letter.)
import string
full_name=input("Enter full name:")
initials=""

for i in full_name:
    if i in string.ascii_uppercase:
        initials+=i+"."
print(initials[:-1])








# # # # # # # # #---------Hard sets-----------

# # # # # # # # #Input a line and print the length of the longest word (words separated by spaces). Ignore multiple spaces.

# # # # # # # # line = input("Enter text:")
# # # # # # # # length = 0
# # # # # # # # max_length = 0

# # # # # # # # for i in line:
# # # # # # # #     if i != " ":   # FIXED HERE
# # # # # # # #         length += 1
# # # # # # # #     else:
# # # # # # # #         if length > max_length:
# # # # # # # #             max_length = length
# # # # # # # #         length = 0   # ALSO IMPORTANT

# # # # # # # # if length > max_length:
# # # # # # # #     max_length = length

# # # # # # # # print(max_length)









# # # # # # # #Input a string and print the most frequent character and its count. (If tie, print the first character that achieves the maximum.)

# # # # # # # import string
# # # # # # # text=input("Enter text:").lower()
# # # # # # # max_count=0
# # # # # # # most_freq_char=""
# # # # # # # for char in string.ascii_lowercase:
# # # # # # #     count=0

# # # # # # #     for i in text:
# # # # # # #         if i==char:
# # # # # # #             count+=1
            
# # # # # # #     if count>max_count:
# # # # # # #         max_count=count
# # # # # # #         most_freq_char=char
           

# # # # # # # print(f"most frequent char is {most_freq_char} with frequency of {max_count}")
    









# # # # # # #Input a string containing ’(’ and ’)’. Print True if parentheses are balanced, else False. (Only check parentheses, ignore other characters.)


# # # # # # text=input("Enter text:")

# # # # # # count_right=0
# # # # # # count_left=0

# # # # # # for i in text:
# # # # # #     if i=="(":
# # # # # #         count_right+=1

# # # # # #     elif i==")":
# # # # # #         count_left+=1

# # # # # #     if count_left>count_right:
# # # # # #         print(False)
# # # # # #         break


# # # # # # if count_right==count_left:
# # # # # #     print(True)

# # # # # # else:
# # # # # #     print(False)









# # # # # #Input a string like: "ab12c3x40" and compute sum of all integers inside it: 12 + 3 + 40 = 55. (No lists.)

# # # # # text="ab12c3x40"
# # # # # sum_digit=0
# # # # # current_digit=0

# # # # # for i in text:

# # # # #     if i.isdigit():
# # # # #         current_digit=0*current_digit+int(i)

# # # # # sum_digit+=current_digit
       

# # # # # print(sum_digit)









# # # # #Input email like "faisal.nadeem@example.com" and output: first character + "***" + domain (keep ’@’ and domain). Example: "f***@example.com". 

# # # # email = input("Enter email: ")

# # # # x = email.find("@")

# # # # masked_email = email[0] + "***" + email[x:]

# # # # print(masked_email)
    






    
# # # #random password generator

# # # import string 
# # # import random

# # # def pass_gen(lenght:int) -> str:
# # #     password=""
# # #     a=string.ascii_letters+string.digits+string.punctuation
# # #     for i in range(lenght):
# # #             g=random.choice(a)
# # #             password+=g

# # #     return f"Random password of lenght {lenght} is {password}"

# # # #Human terminal
# # # password_lenght=10
# # # random_password=pass_gen(password_lenght)
# # # print(random_password)








# # # #Input a password and print True if:
# # # # length >= 8
# # # # contains at least one digit
# # # # contains at least one uppercase letter
# # # # contains at least one lowercase letter
# # # # contains at least one special character from !@#$
# # # # Else print False. (No lists.)


# # import string
# # password=input("Enter password:")
# # upper=0
# # lower=0
# # digit=0
# # pun=0

# # for i in password:

# #     if i in string.digits:
# #         digit+=1
# #     elif i in string.ascii_uppercase:
# #         upper+=1
# #     elif i in string.ascii_lowercase:
# #         lower+=1
# #     elif i in string.punctuation:
# #         pun+=1

# # if (len(password)>=8) and (digit>0) and (lower>0) and (upper>0) and (pun>0):
# #     print(True)
# # else:
# #     print(False)










# #Given: "Sat Jan 5 09:14:16 2008" Extract the hour ("09") using find + slicing, convert to int, and print it.

# inp = "Sat Jan 5 09:14:16 2008"

# x = inp.find(":")
# y = inp.find(":", x + 1)

# hour = inp[x-2:x]

# print(int(hour))
















