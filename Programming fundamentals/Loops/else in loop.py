# # “In a loop, else runs only if the loop didn’t stop early with a break.”

# data = [7, 5, 9, 2, 8, 4, 1]

# for index in range(len(data)):
#     if data[index] == 2:
#         print("Found a 2! Killing the loop.")
#         break  # The loop dies right here.
    
#     print(f"Index {index}: {data[index]}")

# else:
#     print("Else executed as no break statement is used in code!") #if break occurs in loop then else will not be executed


# security_access_codes=[11,22,33,44,55,66]



# for i in range(len(security_access_codes)):

#     enter_security_code=int(input("Enter your security code:"))
#     name=input("Enter your name:")
#     if enter_security_code not in security_access_codes:
#         print(f"Suspecious code entered! arrest {name} which is at index {i}")
#         break

# else:
#     print("Verification completed! No suspecious activity detected!")


for i in range(5):
    
    files=input("Enter file names along with their format:").lower()
    if not files.endswith(".csv"):
        print("Only.csv files are accepted")
        break

else:
    print("All files are .csv")


