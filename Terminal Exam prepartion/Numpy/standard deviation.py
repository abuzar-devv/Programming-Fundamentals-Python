import numpy as np 
import pandas as pd


#----------------------------------------> variation to decide whether std is high , too high / low , low 

#Coefficient of Variation (CV) = (Std Dev / Mean) × 100% -------------------> comparison formula

# CV < 15%       → LOW variation (very consistent) ✅
# 15% ≤ CV < 30% → MODERATE variation (normal) ⚠️
# 30% ≤ CV < 50% → HIGH variation (quite scattered) ❌
# CV ≥ 50%       → VERY HIGH variation (all over the place) 🚨





# Real world application

lenght_of_dataset=int(input("Enter lenght of data set:"))

data_set=np.array([float(input("Enter data:")) for _ in range(lenght_of_dataset)])

variation=(data_set.std/data_set.mean)*100

category_of_variation=np.where((variation>0) & (variation<15),"Low Variation",
                               np.where((variation>=15) & (variation<30),"Moderate variation",
                                        np.where((variation>=30) & (variation<50),"High variation","Very High variation")
                                        
                                        )
                               
                               )

print(f"Mean of data set: {data_set} is {data_set.mean} , its standard deviation is {data_set.std} and its category of variation is {category_of_variation}")