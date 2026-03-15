# Condition controlled loops

# i=int(input("Enter:"))

# while i<5:
#     print(i)
#     i+=1



# entry_codes=[1,2,3,4,5]

# code=int(input("Entry code: "))

# while code in entry_codes:
#     print("You can enter!")
#     break

# else:
#     print("Enter correct code to get permission of entry")


# answer=input("Answer? (yes/No):")

# while answer!='yes':

#     print("Wrong answer!")

#     answer=input("Answer? (yes/No):")


# else:
#     print("Correct answer!")


# attempt=1

# while attempt>=0 and attempt<4:

#     answer=input("Do yoyu agree (yes/no) :").lower().strip()
#     attempt+=1

#     if answer=='yes':
#         print("Glad we are on same page!")
#         break
    
#     else:
#         print("Answer not accepted!")
        

# else:  
#     print("3 Strikes! you are out")


#Gemini practice

#Ticket 1: The POS Loyalty Tracker (Difficulty: Easy)

# Business Context: A coffee shop wants a Point of Sale (POS) system that calculates loyalty points for a single customer's daily transactions.
# 
# Requirements:

# The system must continuously accept transaction amounts (floats) from the cashier.

# If the cashier inputs 0.0, the day's ledger is closed for that customer.

# Every full dollar spent equals 1 loyalty point (e.g., $4.99 is 4 points).

# The system must track the total points accumulated.

# When the ledger closes, output the total points.
# If the total points are 50 or higher, output an additional message alerting the cashier to give the customer a free coffee.


ledger = 0

print("Welcome to Coffee Beans and Tea Leaves POS System")

while True:
    transaction = float(input("Enter transaction amount (0.0 to close ledger): "))

    if transaction == 0.0:
        print("Ledger closed!")
        break

    # Only full dollars count as points
    points = int(transaction)
    ledger += points

    print(f"Points earned from this transaction: {points}")

print(f"Total loyalty points: {ledger}")

if ledger >= 50:
    print("Customer is eligible for a FREE coffee!")












