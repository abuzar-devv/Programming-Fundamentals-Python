#Basic foundations


#Ticket 1: The Cashier's Tally (Accumulator + range + f-strings)
# The Scenario: A customer brings exactly 4 items to the register. You need to calculate their total bill.
# The Requirements: * Use a for loop with range() to run exactly 4 times.

# On every lap, ask the user to enter the price of the item.

# Accumulate the total cost.

# When the loop is finished, print a single f-string showing the grand total formatted to look like real money (2 decimal places).




# total=0

# for i in range(1,5):
#     try:
#         price=float(input(f"Enter the total price of product no {i}:"))
#         total+=price
    
#     except Exception as e:
#         print(e)

# print(f"Total bill of 4 products is: {total}")



#Ticket 2: The Username Scrubber
# Business Requirement: We have a bug in our registration UI where users are accidentally typing numbers into their usernames (e.g., admin123name).
# Write a data-cleaning script that takes a messy username as input.
# The script must process the input and completely discard any numerical digits (0-9). Finally, it should output the sanitized, letters-only version of the username.

# try:

#     username=input("Enter your username:")
#     num='0123456789'
#     clean_username=""

#     for i in username:

#         if i in num:
#             continue

#         else:
#             clean_username+=i


#     print(f"Cleaned version of username is: {clean_username}")

# except Exception as e:
#     print(e)



 
#Ticket 3: The Diagnostic Scanner
#Business Requirement: Write a diagnostic scanner for our factory machines. The program takes a diagnostic code (a string) as input and analyzes it character by character0.
#If it detects the character "x", that indicates a catastrophic hardware failure; the system must print "CRITICAL ERROR" and instantly halt the entire scanning process.
#For any other normal character, it should just print "System stable..." and proceed to check the next one.




# try:

#     diagnostic_code=input("Enter the code:").lower() 
#     index=0

#     for i in diagnostic_code:

#         if i=="x": 
#             print(f"Critical error! at index: {index}")
#             break
#         index+=1

#     print("Stable system!")

# except Exception as e:
#     print(e)




#Ticket 4: The VIP Door System
# Business Requirement: Write the door management software for a private event. The system needs to process a queue of exactly 3 guests.
# For each person, the system must ask for their name and whether they hold a VIP pass.
# The system must collect and store the names of the VIPs. After all 3 guests are processed, 
# the system must output a final report showing the total number of VIPs admitted and displaying their names.

list_of_vip=[]

for i in range(1,4):
    guest=input("Enter your name:").lower()
    vip_pass=input("Do you have vip pass (Yes or no):").lower()
  

    if vip_pass=="yes":

        list_of_vip.append(guest)

print("Total no of vip's:",len(list_of_vip))
print("Vip's are",list_of_vip)

