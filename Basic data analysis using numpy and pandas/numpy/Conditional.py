import numpy as np
import pandas as pd


#-------------------------------------------------Masking (removing un-wanted data)

# marks=np.array([10,90,26,89,50,50,80,28])
# passed=marks[marks>=50]
# print(passed)




# --------------------- conditional logic . np.where(condition, value_if_true, value_if_false)----------------------------------



#Classify each value:

# < 40 → "Fail"
# 40 to 69 → "Pass"
# ≥ 70 → "Excellent"

# 👉 Must use nested np.where()


# marks = np.array([23, 45, 67, 82, 38, 90, 55])

# result=np.where(marks>=70,"Exellent",
#                 np.where((marks>=40) & (marks<70),"pass","fail"))

# print(result)





# # < 30000 → subtract 2000
# # 30000–60000 → add 5000

# # 60000 → add 10000

# # 👉 return updated salary array

# salary = np.array([20000, 45000, 70000, 30000, 90000])

# updated_salary=np.where(salary>=60000,salary+10000,
                        
#                         np.where((salary>=30000) & (salary<=60000),salary+5000,salary-2000)
                        
#                         )
# print(updated_salary)








# #negative values → 0
# values > 100 → 100
# everything else → unchanged

# data = np.array([-5, 10, 120, 75, -20, 200, 50])

# updated_data=np.where(data<0,0,
#                       np.where(data>100,100,data)
#                       )

# print(updated_data)






# #ask:
# < 40 → "Fail"
# 40–69 → "Pass"
# ≥ 70:
# if mark ≥ 90 → "Topper"
# else → "Excellent"

# 3-level + nested inside top category

# marks = np.array([35, 60, 85, 40, 95, 50])

# scholaratic_status=np.where(marks>=90,"Topper",
#                              np.where(marks>69,"Exellent",
#                                      np.where((marks>=40) & (marks<=69),"Pass","Fail"))
#                                      )
# print(scholaratic_status)                            
                           








# #< 200 → no discount
# 200–600 → 10% discount

# 600: 

# if > 1000 → 25% discount
# else → 20% discount

# 👉 return final price


# price = np.array([100, 250, 500, 800, 1200])

# final_price=np.where(price>1000,price-((25/100)*price),
                     
#                      np.where(price>600,price-((20/100)*price),
#                      np.where((price>=200) & (price<=600),price-((10/100)*price),price)))

# print(final_price)