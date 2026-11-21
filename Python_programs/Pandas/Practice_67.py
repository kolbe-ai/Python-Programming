"""
67. Using the given employee data
(Name, Department, Salary:
John/HR/45000,
Alice/IT/55000,
Bob/HR/40000,
David/IT/60000,
Emma/Finance/50000):
(a) create a DataFrame,
(b) add a Bonus column equal to 10% of salary,
(c) group by Department and find the average salary,
(d) add a Category column using a function (“High” if Salary ≥ 50000, else “Low”),
(e) use boolean indexing to show employees earning more than 45000.
"""

import pandas as pd
#a
data = {"Name": ["John","Alice","Bob","David","Emma"],"Department" : ["HR","IT","HR","IT","Finance"],"Salary": [45000,55000,40000,60000,50000]}
data_frame = pd.DataFrame(data)
print("\n\nData: \n",data_frame)

#b
data_frame["bonus"] = data_frame["Salary"] *10/100
print("\n\nData after adding bonus: \n",data_frame)

#c
grp_data_frame = data_frame.groupby("Department")["Salary"].mean()
print("\n\nGrouped data: \n",grp_data_frame)

#d
level = []
for i in data_frame["Salary"]:
    if i>= 50000:
        level.append("High")
    else:
        level.append("Low")
data_frame["Level"] = level
print("\n\nNew Data is: \n",data_frame)
#e
print("\n\nEmployee above 45000\n")
print(data_frame[data_frame["Salary"]>=45000])