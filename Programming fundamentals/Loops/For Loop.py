#For loops (Count-controlled loops)

# for i in range(1,2):
#     print(i)

# for i in (9,0,1):
#     i=i+6            #it will take i and will add 6 and will give final output in print
#     print(i)


# for i in range(1,15,2):  #range(start,stop,step)
#     print("Round",i,":")


# rounds=(1,2,3,4,5)

# for i in rounds:
#     print(f"Round {i}:")

# word=input("Enter a word:")

# count=1

# for i in word:
#     print(f"word no {count} is {i}")
#     count+=1

#Check vovels one by one

# sentence=input("Enter a sentence:").lower()
# vowels="aeiou"
# vowels_in_sentence=[]

# for i in sentence:

#     if i==" ":              #it will skip spaces
#         continue

#     if i in vowels:

#         vowels_in_sentence.append(i)
#         print(f"{i} is a vowel.")

#     else:
#         print(f"{i} is not a vowel.")

# total_vowels_in_sentence=len(vowels_in_sentence)
# print(vowels_in_sentence)
# print(total_vowels_in_sentence)



#Average marks for all class and class grade.



# obtained_marks=0
# total_students=int(input("Enter the total no of students:"))
# total_marks_of_test=float(input("Enter the total marks of the test:"))
# total_marks_whole_class=total_marks_of_test*total_students

# good_students=[]
# average_students=[]
# poor_students=[]
# faulty=[]

# try:

#     for i in range(1,total_students+1):

#         roll_marks=float(input(f"Roll no {i} enter your marks, total marks of test are {total_marks_of_test} :"))
       

#         if roll_marks>total_marks_of_test or roll_marks <0:
             
#              print("Obtained marks cannot exceed total marks or cannot be less than zero, marks not counted ")
#              faulty_roll=input("Enter your roll no.")
#              faulty.append(faulty_roll)


#         if roll_marks<=total_marks_of_test and roll_marks>=0:
#                       obtained_marks+=roll_marks

             

#             #Student assesment


#         percentage_per_student=(roll_marks/total_marks_of_test)*100

#         if percentage_per_student>=0 and percentage_per_student<=100:
    
#             name=input("Enter your name and roll number (format: My name is x and roll no is y) :")

#             if percentage_per_student>=80 and percentage_per_student<=100:
                    
#                     good_students.append(name)
#                     print("Exellent performance!")

#             elif percentage_per_student>=60 and percentage_per_student<80:
                    
#                     average_students.append(name)
#                     print("Performance is satisfactory. Do more!")

#             elif percentage_per_student>=0 and percentage_per_student<60:
                    
#                     poor_students.append(name)
#                     print("Nill performace. much improvement needed!")

#             else:
#                 print("Invalid input!")

#         else:
#               print("Your roll no is already noted")

#     percentage_of_class=(obtained_marks/total_marks_whole_class)*100

#     if percentage_of_class>=85:
#         print(f"Exellent class they have got class percentage of {percentage_of_class}")

#     elif percentage_of_class>=70 and percentage_of_class<85:
#         print(f"Good class , they have got the class percentage of {percentage_of_class}")

#     elif percentage_of_class>60 and percentage_of_class<70:
#         print(f"Not good")

#     else:
#         print("Fail! much improvement needed not good result overall!")


#     print(f"This is list of good students = {good_students}")
#     print(f"This is list of average students = {average_students}")
#     print(f"This is list of poor students = {poor_students}")
#     print(f"These are faulty roll no = {faulty}")

# except Exception as e:
#      print("Error is:",e)


#tables generator 

# try:
#     table_num=int(input("Enter the digit whom we will print table:"))
#     num=int(input("Enter the digit till which we will print table:"))

#     for i in range(1,num+1):
#           calc=table_num*i
#           print(f"{table_num} * {i} = {calc}")

# except Exception as e:
#       print(f"Error is {e}")


#Rows of * (increasing in each row) 

# symbol="*"
# rows=int(input("Enter the number of rows that we have to print:"))

# for i in range(1,rows+1):
            
#             print(symbol)
#             symbol+="*"


#Same in coutomized way

# sym=input("Enter symbol you want to print:").strip().lower()
# rows=int(input("Enter the no of rows you want to print"))

# for i in range(1,rows+1):

#     print(sym*i)





files_list=[]
no_of_files=int(input("Enter the number of files that you will input:"))

for i in range(1,no_of_files+1):

    file=input("Enter file name ending with file format: ").lower()

    if file in files_list:
        print(f"Duplicate files {file} found that might cause severe error so loop is broke!")
        break

    files_list.append(file)

else:
    print("Scan completed no duplication found")
    print(f"List of files: {files_list}")















