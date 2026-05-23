#new implementations needed

obtained_marks=0
total_students=int(input("Enter the total no of students:"))
total_marks_of_test=float(input("Enter the total marks of the test:"))
total_marks_whole_class=total_marks_of_test*total_students

good_students=[]
average_students=[]
poor_students=[]
faulty=[]

try:

    for i in range(1,total_students+1):

        roll_marks=float(input(f"Roll no {i} enter your marks, total marks of test are {total_marks_of_test} :"))
       

        if roll_marks>total_marks_of_test or roll_marks <0:
             
             print("Obtained marks cannot exceed total marks or cannot be less than zero, marks not counted ")
             faulty_roll=input("Enter your roll no.")
             faulty.append(faulty_roll)


        if roll_marks<=total_marks_of_test and roll_marks>=0:
                      obtained_marks+=roll_marks

             

            #Student assesment


        percentage_per_student=(roll_marks/total_marks_of_test)*100

        if percentage_per_student>=0 and percentage_per_student<=100:
    
            name=input("Enter your name and roll number (format: My name is x and roll no is y) :")

            if percentage_per_student>=80 and percentage_per_student<=100:
                    
                    good_students.append(name)
                    print("Exellent performance!")

            elif percentage_per_student>=60 and percentage_per_student<80:
                    
                    average_students.append(name)
                    print("Performance is satisfactory. Do more!")

            elif percentage_per_student>=0 and percentage_per_student<60:
                    
                    poor_students.append(name)
                    print("Nill performace. much improvement needed!")

            else:
                print("Invalid input!")

        else:
              print("Your roll no is already noted")

    percentage_of_class=(obtained_marks/total_marks_whole_class)*100

    if percentage_of_class>=85:
        print(f"Exellent class they have got class percentage of {percentage_of_class}")

    elif percentage_of_class>=70 and percentage_of_class<85:
        print(f"Good class , they have got the class percentage of {percentage_of_class}")

    elif percentage_of_class>60 and percentage_of_class<70:
        print(f"Not good")

    else:
        print("Fail! much improvement needed not good result overall!")


    print(f"This is list of good students = {good_students}")
    print(f"This is list of average students = {average_students}")
    print(f"This is list of poor students = {poor_students}")
    print(f"These are faulty roll no = {faulty}")

except Exception as e:
     print("Error is:",e)