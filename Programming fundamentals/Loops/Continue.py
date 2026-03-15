#We use continue to skip bad data instead of stopping the loop. For stopping the loops we use break.


# names=["ali","ahmad","","abuzar"]

# for name in names:
#     if name=="":
#         print("Empty space detected!")
#         continue

#     print(f"Name={name}")



days=["monday","tuesday","wednesday","saturday","sunday"]
weekend=["saturday","sunday"]

for day in days:
    if day in weekend:
        continue
    print(f"working day : {day}")