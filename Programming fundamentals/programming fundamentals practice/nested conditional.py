# # # 1- The Cinema Kiosk: A customer wants to buy a movie ticket. Check if their age is 18 or older. 
# # # If they are, check if they have a student ID.



# # #Solution


# # print("Welcome to cinema!")

# # print("Press 0 as No and 1 as Yes")



# # user_input=int(input("Want to buy a movie ticket? :"))


# # if user_input==1:
# #     age=int(input("Enter age:"))

# #     student_id=int(input("Do you have a student id? :"))

# #     if age>=18:
# #         if student_id==1:
# #             print("You can get discount on student id as youy are above 18!")
# #         else:
# #             print("you're above 18 but you cannot get student Id discount!")
# #     elif age<18:
# #         if student_id==1:
# #             print("Enjoy your movies with a student discount! (cannot watch 18+ movies!)")
# #         else:
# #             print("Enjoy your movie! (cannot watch 18+ movies)")

# # else:
# #     print("No ticket bought!")
    



# # #2- Here is your scenario again:

# # The Basic Login System: A user tries to log in. First, check if their entered username matches the system's database.
# # If it does, check if their entered password matches.

# # Your Mission:
# # Hardcode a "correct" username and password at the top of your script (this will act as your database).

# # Ask the user to input their username.

# # Outer Condition: Check if the username matches your database.

# # Inner Condition (Nested): If the username is correct, ask for their password and check if it matches.



# #Solution



# # print("Welcome back!")

# correct_username="Abuzar"
# correct_password="A2208@@"

# enter_username=input("Enter your user-name:")

# if enter_username==correct_username:
#     enter_password=input("Enter password! :")
#     if enter_password==correct_password:
#         print("login successfull!")
#     else:
#         print("Enter correct password!")

# else:
#     print("Enter correct username!")




# 3- Question 3: The E-Commerce Shipping Calculator
# A customer is checking out of an online store.

# Ask the user to input their total cart value (a number).

# If the cart value is $100 or more: They automatically qualify for "Free Premium Shipping." Print this message.

# If the cart value is less than $100: You must now check their membership status to determine their shipping cost.

# Ask them: "Are you a Premium Member? (Press 1 for Yes, 0 for No)"

# If they press 1: Print "You get Free Standard Shipping."

# If they press 0: Print "Shipping costs $10."

# Your Constraints (Read Carefully):


# Strict Lazy Evaluation: You are strictly forbidden from asking the user for their membership status at the beginning of the program.
# If their cart is $150, asking them if they are a member wastes the user's time and the computer's memory.
# You must only ask for membership if the cart is under $100.



# No Redundancy: If the cart is not $100 or more, do not force the computer to calculate if it is less than $100.
# Use the correct catch-all statement.


# total_cart_value=float(input("Enter total cart value (in digits) :"))

# if total_cart_value >=100:
#     print("Enjoy free premium shipping!")

# else:
#     print("Enter 1 for yes and 0 for no")

#     membership=int(input("Are you a premium member? :"))

#     if membership==1:
#         print("You get Free Standard Shipping")
#     elif membership>1 or membership<0:
#         print("Enter valid value (0 or 1)")
#     elif membership==0:
#         print("Shipping costs $10.")


# print("Thanks for shopping!")



# Category 2: Medium (Deep Nesting)
# We are moving to three levels of nested logic.

# Medium Question 1: The Bank Loan Approver:

# A customer applies for a bank loan. You must evaluate them strictly step-by-step.
# If they fail at any stage, reject them immediately and do not ask them any further questions.

# Ask the user for their Credit Score (a number).

# If their credit score is less than 700: Print "Loan Denied: Credit score too low."

# If their credit score is 700 or higher: You need more information.

# Now, ask for their Monthly Income (a number).

# If their income is less than $5000: Print "Loan Denied: Income insufficient."

# If their income is $5000 or higher: You need one final check.

# Now, ask them: "Do you have an existing loan? (1 for Yes, 0 for No)"

# If they press 1 (Yes): Print "Loan Denied: Please pay off your existing loan first."

# If they press 0 (No): Print "Congratulations! Loan Approved."

# (Apply the industry standard validation here: use else for invalid inputs).

# Your Constraints:

# Extreme Lazy Evaluation: Do not ask for income if their credit score is bad. Do not ask about existing loans if their income is bad.

# Deep Nesting: This requires three levels of logic. One if inside an if inside an if. Pay extreme attention to your indentation.
# If your indentation is wrong, your logic breaks.



# print("Welcome to Meezan Bank Loan Service")

# credit_score=float(input("Enter your credit score (in digits) :"))

# if credit_score<700:
#     print("Loan Denied: Credit score too low")

# else:
#     print("We need more information")
#     income=float(input("Enter your monthly income :"))
#     if income<5000:
#         print("Loan Denied: Income insufficient")
    
#     else: 
#         print("We need one final check!")
#         print("Enter 0 for NO and 1 for YES")
#         existing_loan=int(input("Do you have an existing loan? :"))
#         if existing_loan == 1 :
#             print("Loan Denied: Please pay off your existing loan first")
        
#         elif existing_loan==0:
#             print("Congratulations! Loan Approved.")
        
#         else:
#             print("Enter valid value!")

# feedback=float(input("How was your experience? (Press 1 if satisfied 0 if not) :"))
# if feedback==0:
#     complain=input("Enter your complain:")
#     print("Complain noted!")

# elif feedback==1:
#     print("Thanks for your feedback!")
# else:
#     print("Enter valid value!")      
    
# print("Thanks for choosing us!")




# #Medium Question 2: The Employee Bonus System
# It is the end of the year, and a company is calculating employee bonuses based on two things: Years of Service and Performance Rating.

# Ask the user for their Years of Service (a number).

# Ask the user for their Performance Rating. (Tell them to type either "Excellent" or "Good" or "Poor").
# (Note: HR always needs both of these pieces of information upfront, so ask for both of these inputs at the very top.
# No lazy evaluation needed for the inputs this time).

# The Logic Rules:

# If they have been with the company for MORE than 3 years:

# If their rating is exactly "Excellent", print: "Bonus: 20% of salary."

# If their rating is exactly "Good", print: "Bonus: 10% of salary."

# If their rating is exactly "Poor", print: "Bonus: 0%. Performance improvement plan required."

# (Catch invalid text input here: If they type "Average" or anything else, print "Invalid rating entered.")

# If they have been with the company for 3 YEARS OR LESS:

# If their rating is exactly "Excellent", print: "Bonus: 5% of salary."

# If their rating is anything else (Good, Poor, Average, etc.), print: "Bonus: 0%. Standard vesting period applies."

# Your Directives:

# Exact String Matching: Python is case-sensitive. if rating == "Excellent": is not the same as if rating == "excellent":.

# Operator Precision: Pay close attention to "MORE than 3 years" versus "3 YEARS OR LESS". Use > and <= correctly.

# Nesting: You will have an outer if-else for the years, and inner if-elif-else blocks for the text matching.



# print("Welcome!")

# years_of_service=float(input("Enter your years of experience (in numbers):"))

# performance_rating=input('type either "Excellent" or "Good" or "Poor :').lower()


# if years_of_service > 3:
#     if performance_rating=="excellent":
#         print("Bonus: 20% of salary.")
#     elif performance_rating=="good":
#         print("Bonus: 10% of salary.")
#     elif performance_rating=="poor":
#         print("Bonus: 0%. Performance improvement plan required")    
#     else:
#         print("Enter valid rating! (0,1,2) ")


# else:

#         if performance_rating=="excellent":
#          print("Bonus: 5% of salary.")

#         else:
#          print("Bonus: 0%. Standard vesting period applies.")










# #The Final Exam: The High-Security Bank Transfer System
# You are writing the backend logic for a bank's wire transfer system.

# Step 1: Account Type

# Ask the user for their account type. They must type "Personal" or "Business".

# Sanitize this input. The system must accept "personal", "PERSONAL", etc.

# If they type anything else, print: "Error: Invalid account type." and stop. Do not ask them any further questions.

# Step 2: Personal Account Logic

# If they chose "Personal", ask for the Transfer Amount (must handle decimals).

# If the amount is strictly greater than $5,000: Print "Transfer Denied: Exceeds personal limit." (Do not ask for a PIN).

# If the amount is $5,000 or less: * Now ask for their 4-digit PIN (a whole number).

# If the PIN is exactly 1234, print: "Transfer Approved."

# For any other PIN, print: "Transfer Denied: Incorrect PIN."

# Step 3: Business Account Logic

# If they chose "Business", the bank needs to know where the money is going. Ask for the Transfer Destination: "Domestic" or "International".

# Sanitize this input too. * If "Domestic":

# Ask for their Transfer Amount (handle decimals).

# Domestic business transfers have no limits.
# Simply print: "Domestic transfer of $[amount] authorized.
# " (You don't need to format the exact string perfectly, just print a success message).

# If "International":

# International transfers require a strict security clearance. Do not ask for the transfer amount.

# Instead, ask for the Authorization Code.

# Security Trap: Passwords and codes are strict. DO NOT sanitize this. It must be exactly "ALPHA-7". If they type "alpha-7", it is wrong.

# If the code is exactly "ALPHA-7", print: "International Transfer Approved."

# If the code is anything else, print: "CRITICAL: Invalid code. Account locked."

# If they type a destination other than Domestic or International, print "Error: Invalid destination."

# Your Directives (The Grading Rubric):
# Zero Redundancy: If I am doing a Personal transfer of $10,000, your program better not ask me for my PIN.

# Data Types: Use float for money. Use int for the PIN. Use strings for the words.

# Black Holes: Every if and elif must have a corresponding else to catch bad data.

# No Loops or Advanced Functions: You must build this entirely out of if, elif, else, input(), int(), float(), and .lower().




# account_type=input("Enter your account type (Personal or Business) :").lower()


# if account_type=="personal":

#     transfer_amount=float(input("Enter Transfer Amount (Digits):"))

#     if transfer_amount > 5000:

#         print("Transfer Denied: Exceeds personal limit." )

#     else:
#         pin_code=int(input("Enter your 4-Digit pin code :"))

#         if pin_code==1234:

#             print("Transfer Approved.")
#         else:
#             print("Transfer Denied: Incorrect PIN.")

# elif account_type=="business":
#     transfer_destination_bussiess_account=input("Transfer Destination: Domestic or International :").lower()

#     if transfer_destination_bussiess_account=="domestic":

#         bussiness_account_transfer_amount=float(input("Enter transfer amount:"))

#         print("Domestic transfer of", bussiness_account_transfer_amount, "authorized")

#     elif transfer_destination_bussiess_account=="international":

#         authorization_code=input("Enter authorization code:")

#         if authorization_code=="ALPHA-7":

#             print("International Transfer Approved.")

#         else:
#             print("CRITICAL: Invalid code. Account locked.")

#     else:
#         print("Error: Invalid destination.")

# else:
#     print("Enter valid account type!")




# print("Thanks for using our banking service!")






#Hard Question 2: The Timeline Collision (Meeting Scheduler)
# This is a classic whiteboard interview question for junior engineers.
# It tests your ability to think about abstract boundaries and overlapping states.

# You are building the logic for a calendar app. A user is trying to schedule two meetings on the same day.
# You must determine if the meetings conflict.

# The Inputs:
# Ask the user for four separate integers (Assume a 24-hour clock, 0 to 24):

# meeting_1_start

# meeting_1_end

# meeting_2_start

# meeting_2_end

# The Logic Rules:

# Input Validation (Lazy Evaluation): * A meeting's start time must be strictly less than its end time.
# If meeting_1_start is 14 and meeting_1_end is 12, print "Error: Invalid timeline." and stop.

# All times must be between 0 and 24 (inclusive). If they type 25, print "Error: Invalid hour." and stop.

# The Conflict Check:

# Determine if the two meetings overlap in time.

# Note: If Meeting 1 ends exactly when Meeting 2 starts (e.g., M1 is 9 to 11, M2 is 11 to 13), this is NOT a conflict.
# They are just back-to-back.

# If they overlap, print: "Schedule Conflict: Meetings overlap."

# If they do not overlap, print: "Schedule Clear."

# Your Directives (Read Carefully):

# Do not write 15 different if/elif statements trying to guess every possible combination of hours.
# There is a clean, mathematical way to compare two timelines to see if they cross. Think about the boundaries.

# Use your logical operators (and, or) to combine conditions efficiently.

# If the inputs are invalid, do not run the conflict check.




# print("Enter meeting timings (24-Hours clock only)")

# meeting_1_start=int(input("Enter meeting 1 starting time:"))

# meeting_1_end=int(input("Enter meeting 1 ending time:"))

# meeting_2_start=int(input("Enter meeting 2 starting time:"))

# meeting_2_end=int(input("Enter meeting 2 ending time:"))

# if (meeting_1_start>24) or (meeting_1_end >24) or (meeting_2_start>24) or (meeting_2_end>24):
#     print("Error: Invalid hour.")

# else:   
#     if (meeting_1_start>meeting_1_end) or (meeting_2_start>meeting_2_end):
#         print("Error! meeting starting time cannot be greater than meeting ending time")

#     elif (meeting_1_start==meeting_1_end) or (meeting_2_start==meeting_2_end):
#         print("0 meeting time error")   

#     elif  meeting_1_start > meeting_2_start:
#         print("Error meeting 2 can not occur before meeting 1")
     

#     elif (meeting_1_start==meeting_2_start) or (meeting_2_start<meeting_1_end):
#         print("Conflict between meetings!")

#     else:
#         print("Schedule Clear.")







# #The Final Problem: The Geometry Engine
# You are writing the core logic for a geometry application. The user will give you the lengths of three lines.
# Your program must determine if those lines can physically form a triangle, and if so, what kind of triangle it is.

# The Inputs:
# Ask the user for three separate numbers: side_a, side_b, and side_c (treat them as integers).

# The Rules of the Universe (The Constraints):

# The Reality Constraint: A line cannot have a length of 0 or a negative number.

# The Physics Constraint
# (Triangle Inequality Theorem):
# For a triangle to physically exist, the sum of the lengths of any two sides must be strictly greater than the length of the third side.
# If I give you lines of length 1, 2, and 10, they cannot connect to form a triangle.

# The Classifications:

# If all three sides are exactly the same length, it is Equilateral.

# If exactly two sides are the same length, it is Isosceles.

# If all three sides are completely different lengths, it is Scalene.

# Your Only Directive:
# Your program must print exactly one correct outcome for whatever the user types.
# It should tell the user if the inputs are invalid, if the triangle is physically impossible, or what specific type of triangle it is.




print("Welcome to geometric simualator")

print("Input the sides of triange as integer values (1,2,3.....)")

side_a=int(input("Enter the lenght of side A (should be integer!) :"))
side_b=int(input("Enter the lenght of side B (should be integer!) :"))
side_c=int(input("Enter the lenght of side C (should be integer!) :"))


if (side_a<=0) or (side_b<=0) or (side_c<=0):
    print("Enter +ve integers only!")

elif (side_a+side_b <= side_c) or (side_a+side_c<=side_b) or (side_b+side_c<=side_a):
    print("triangle to physically exist, the sum of the lengths of any two sides must be strictly greater than the length of the third side")

elif (side_a==side_b==side_c):
    print("It is a equilateral triangle")

elif (side_a==side_b) or (side_a==side_c) or (side_b==side_c):
    print("It is a isoceles triangle!")

else:
    print("it is a scelene triangle")




























