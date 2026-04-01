# # # def make_coffee():
# # #     coffee=input("which coffee would you prefer? :").lower().strip()

# # #     if coffee=="expresso" or coffee=="americano":
# # #         print("It will have a bold strong taste!")
# # #         print("Enjoy your cup of coffee!")

# # #     elif coffee=="latte":
# # #         print("It will be less stronger than expresso!")
# # #         print("Enjoy your cup of coffee!")

# # #     else:
# # #         print("Not available!")

    



# # # # print("Welcome to Coffee Planet!")
# # # # make_coffee()


# # # # #Mathematical equation
# # # # def f(x, y):
# # # #     eq=(2*x + 6*y - 26) / 100

# # # #     return eq
    

# # # # a = float(input("Enter x: "))
# # # # b  = float(input("Enter y: "))

# # # # print(f(a, b))




# # # #Basic practice

# # # #Build a checkout calculator for our storefront. The cashier needs to process three separate items per customer.
# # # #The system must accept the raw price of each item, apply a mandatory 8% regional sales tax, and display the final taxed price for each individual item.
# # # #After processing all three items, the system must display the grand total of the entire order.
# # # #The system must not crash if the cashier accidentally scans a barcode into the price field instead of typing a number.


# # # def apply_tax(items):

# # #     try:
# # #         total=0
# # #         # items=int(input("Enter the total number of items"))

# # #         for i in range(1,items+1):
# # #             price=float(input("Enter price of product:"))
# # #             after_tax=price+((8/100)*price)
# # #             total+=after_tax
# # #             print(f"Price of this item after tax is {after_tax}")

# # #     except Exception as e:
# # #         print(f"Error is {e}")

# # #     return  print(f"Total price of {items} items after 8% tax is {total}")

    


# # # items=int(input("Enter number of items:"))

# # # apply_tax(items)


# # # #Better code


# # def apply_tax(items):
# #     total = 0

# #     for i in range(1, items + 1):
# #         try:
# #             price = float(input("Enter price of product: "))
# #         except:
# #             print("Invalid input! Try again.")
# #             continue

# #         after_tax = price + (0.08 * price)
# #         total += after_tax

# #         print("Price after tax is:", after_tax)

# #     print("Total price of", items, "items after 8% tax is", total)
# #     return total


# # # items = int(input("Enter number of items: "))
# # apply_tax(3)





# # # # Business Requirement:
# # # Design an RFID security gate protocol for the main server room. Employees scan numeric ID badges to open the secure door. 
# # # The gate mechanism uses a rudimentary hardware checksum: an ID is only authorized for entry if its absolute last digit is an even number.

# # # Simulate three consecutive employees swiping their badges. 
# # # For each badge scan, the system must evaluate the badge and output either "Access Granted" or "Access Denied". 
# # # The system must be robust enough to cleanly reject non-numeric badge scans (e.g., corrupted card reads returning text)
# # # without taking the security server offline, forcing the employee to rescan.


# # def security_scan():
# #     employee_no=1

# #     for i in range(1,4):
# #         try:
# #             security_code=int(input("Enter security pass:"))
           
# #             last_dig=security_code%10

# #             if last_dig%2==0:
# #                 print(f"Access granted to employee no {employee_no}")

# #             else:
# #                 print(f"Access denied to employee no {employee_no}")

# #             employee_no+=1
# #         except Exception as e:
# #             print(f"Error is {e}")

# # security_scan()

# # print(globals())
# # print(locals())





# #-----------Default parameter------------

# # def info(name,age:int,country="pakistan") -> str | int:
# #     result=f"My name is {name} , age is {age} and i am from {country}"
# #     print(result)
# #     return result

# # info("abuzar",19)


# Ticket 2: The "Mystery Cart" Checkout System (Hard)
# The Business Requirement (From Marketing):
# "Hey team, we need a new checkout function for the Mystery Sale. It needs to take the customer's full name and whatever items they are buying. But wait, "
# "our database keeps crashing because people type weird spaces in their names, "
# "so make sure the function strips out every single space and makes their name completely uppercase before it does anything else. Also, "
# "if they try to check out with zero items, the function should just instantly abort and send back a message saying the cart is empty."
# "Assuming they actually bought stuff, add up all the prices. "
# "Then, here is the fun part: the system needs to 'roll the dice' and pick a random discount between 10% and 40% for them."
# "Apply that discount to their total, and send back a formatted receipt string."
# " Oh, and build a terminal prompt so the cashier can type the names in safely without the app crashing."

# The Exact Output I Expect From Your Factory:
# If I call your function like this: checkout_system("John Doe", 100.0, 50.0)
# And the random dice roll happens to land on 20, your function must return exactly this string:

# "RECEIPT | Customer: JOHNDOE | Original Total: $150.0 | Discount Won: 20% | Final Price: $120.0"

# The Terminal Execution Constraint:
# Your factory must be pure. Outside the factory, you must build a while True: loop. 
# Ask the cashier to input() the customer's name. Wrap the factory call in a try/except Exception: block so the system is crash-proof.
# Pass the inputted name and a few hardcoded float prices into your function. Print the returned receipt, then break the loop.


import random

def checkout(name:str,*items:float) -> str:

            if len(items)==0:
                return "0 items were added in the cart!"
            
            total=sum(items)
            
            clean_name=name.replace(" ","")

            discount_percentage=random.randint(10,40)

            after_discount=(total)-((discount_percentage/100)*total)

            return f"RECEIPT | Customer: {clean_name.upper()} | Original Total: {total} | Discount Won: {discount_percentage} | Final Price: {after_discount:.2f}"



while True: 
        cashier_input=input("Enter name:")

        try:
            result=checkout(cashier_input,101,99.6)
            print(result)
            break

        except Exception as e:
               print("Bad data! Try again paglu")