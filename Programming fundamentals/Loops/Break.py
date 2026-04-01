#The break statement is a permanent kill switch that instantly terminates the entire loop, abandoning all remaining items.


data = [7, 5, 9, 2, 8, 4, 1]

for index in range(len(data)):
    if data[index] == 2:
        print("Found a 2! Killing the loop.")
        break  # The loop dies right here.
    
    print(f"Index {index}: {data[index]}")

# OUTPUT: 
# Index 0: 7
# Index 1: 5
# Index 2: 9
# Found a 2! Killing the loop.
# (Notice 8, 4, and 1 are never printed. The loop is gone.)


#Gemini practice questions.
names_list = []

persons = int(input("Enter the number of persons:"))

for i in range(persons):  # remove the +1 to avoid extra iteration
    names = input("Enter names:").lower()
    names_list.append(names)

    if "ali" in names_list:  # check for suspect
        print("Suspect detected!")
        break  # stop the loop immediately

# Get the exact index of "ali" in the list (safer than using i)
if "ali" in names_list:
    index = names_list.index("ali")
    print(f"Index of ali in list is: {index}")

print(f"List of names is: {names_list}")
print("Loop ended!")