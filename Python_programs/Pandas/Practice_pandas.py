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

data = {"Name" : ["John","Alice","Bob","David","Emma"] ,"Department" : ["HR","IT","HR","IT","Finance"], "Salary" : [45000,50000,40000,60000,50000]}
dataa = pd.DataFrame(data)
print(dataa)

dataa["Bonus"] = dataa["Salary"] *.10
print(dataa)

grouped_data = dataa.groupby("Department")["Salary"].mean()
print(grouped_data)

level = []
for i in dataa["Salary"]:
    if i>= 50000:
        level.append("High")
    else:
        level.append("Low")
dataa["Level"] = level
print(dataa)
print(dataa[dataa["Salary"] >45000])