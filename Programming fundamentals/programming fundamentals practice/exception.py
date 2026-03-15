#Easy




#Scenario 1: The Bouncer (Testing ValueError)
# The Industry Reality: Users cannot read instructions. If you ask for a number, they will type a word.
# The Task:

# Ask the user for their age.

# If they type a word (e.g., "Twenty"), catch the explosion using ValueError and print: "System Crash Averted: Please enter digits only."

# # The Logic: If the input succeeds, use an if/elif/else waterfall. If age is less than 0, print "Invalid age."
# # If age is 18 or older, print "Access Granted." Otherwise, print "Access Denied."




# try:
#     age=float(input("Enter your age:"))

#     if age >=18:
#         print("Access granted!")
#     elif age<0:
#         print("Invalid age!")
#     else:
#         print("Access denied!")    


# except ValueError:
#     print( "System Crash Averted: Please enter digits only.")


# except Exception as e:
#     # THE ULTIMATE SAFETY NET
#     # If ANY other error happens that we didn't predict, this catches it.
#     print("CRITICAL: An unknown error occurred. The system survived.")
#     print("Here is what went wrong:", e)





#Scenario 2: The Split Bill
# Here are your exact requirements. Read them carefully before you write a single line.

# The Setup: Hardcode a variable at the top of your try block: bill = 100

# The Danger Zone: Ask the user: "How many people are splitting the bill?" (convert this to an integer).

# The Math: Calculate the cost per person (bill / people).

# The Business Logic: * If the cost per person is strictly greater than $20, print: "That's an expensive meal."

# Else, print: "Cheap meal."

# The Bomb Squads: * You need an except ValueError: to catch users who type words (like "five").

# You need a separate except ZeroDivisionError: to catch users who type 0. Tell them "Error: Cannot divide a bill by zero people."




try:
    bill=100

    people=int(input("How many people are splitting the bill? :"))

    bill_per_person=(bill/people)
    
    if bill_per_person>20:
        print("That's an expensive meal.")

    else:
        print("Cheap meal")

except ValueError:
    print("Enter numerical value (integer) !  (Value error)")

except ZeroDivisionError:
    print("People must me >0  (zero division error)")

except Exception as e:
    print("Here is what went wrong:", e)



#Medium




#Medium Scenario 1: The Cloud Server Provisioner
# You are writing the backend script for a cloud hosting company. A user is trying to rent a server and allocate RAM (memory) to it.

# The Directives:

# 1. The Setup & Connection (Outside the Danger Zone)

# The absolute first thing your program must do is print: "--- Initiating Secure Server Connection ---"

# 2. The Danger Zone (The Inputs)

# Ask the user for the Server ID (Must convert to an int).

# Ask the user for the Memory Requested in GB (Must convert to a float, because they might ask for 16.5 GB).

# 3. The Exception Handlers (The Shields)

# Catch ValueError if they type text (like "sixteen") instead of numbers. Print: "Crash Averted: Inputs must be numeric."

# Catch the ultimate Exception as e at the bottom. Print "Critical System Failure: ", e

# 4. The Business Logic (Nested Conditionals inside the try)

# If the Server ID is 101 (Standard Server):

# Check the memory. If memory is <= 0, print "Error: Cannot allocate zero or negative memory."

# Else if memory is > 64, print "Error: Server 101 max capacity is 64GB."

# Else, print "Server 101 successfully provisioned with [X] GB."

# If the Server ID is 202 (High-Performance Server):

# Check the memory. If memory is <= 0, print "Error: Cannot allocate zero or negative memory."

# Else if memory is > 256, print "Error: Server 202 max capacity is 256GB."

# Else, print "Server 202 successfully provisioned with [X] GB."

# If they type any other Server ID (e.g., 999):

# Print "Error: Unknown Server ID."

# 5. The Janitor (The Mandatory Cleanup)

# You skipped practicing this, so prove you know it. You MUST use a finally block at the absolute end of the script.
# It must print: "--- Server Connection Terminated ---"

# This message must print if the server successfully provisions, if the user types a negative number,
# AND if the user types the word "Apple" and triggers an exception. It must run 100% of the time.

# Your Constraints
# You are now juggling:

# Two different data type conversions (int and float).

# Dual-layer Exception handling.

# Nested Conditionals (Conditionals inside of Conditionals).

# Unconditional resource cleanup.









































