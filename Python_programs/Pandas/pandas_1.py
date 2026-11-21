"""
Name, Dept, Salary, Rating →
(Ravi, IT, 60000, 4.5),
(Sita, HR, 45000, 3.8),
(Mohan, IT, 70000, 4.2),
(Latha, Sales, 40000, 3.5),
(Arun, HR, 48000, 4.0)

(Pandas: DataFrame + apply()) [PDF Q67] Create the DataFrame, add Tax = 12% of salary,
and add Level (“Senior” if salary ≥ 55000 else “Junior”) using a function with apply().
(Pandas: GroupBy, Boolean Indexing, Sorting) [PDF Q67-68] Print the average salary per Dept,
employees with Rating > 4.0, and the DataFrame sorted by Salary descending.
"""

import pandas as pd

employee = {"Name": ["Ravi","Sita","Mohan","Latha","Arun"],
            "Dept" : ["IT","HR","IT","Sales","HR"],
            "Salary" : [60000,45000,70000,40000,48000],
            "Rating": [4.5,3.8,4.2,3.5,4.0]}

#Create the DataFrame
data = pd.DataFrame(employee)
print(data)

#add Tax = 12% of salary
print("\n\n")
data["Tax"] = data["Salary"] *.12
print(data)

#add Level (“Senior” if salary ≥ 55000 else “Junior”) using a function with apply().
level = []
def apply(data):
    for i in data["Salary"]:
        if i>=55000:
            level.append("Junior")
        else:
            level.append("Senior")
apply(data)
data["Level"] = level
print("\n\n")
print(data)

#(Pandas: GroupBy, Boolean Indexing, Sorting) [PDF Q67-68] Print the average salary per Dept,
#employees with Rating > 4.0, and the DataFrame sorted by Salary descending.
print("\n\n")
avg = data.groupby("Dept")["Salary"].mean()
print(avg)

print("\n\n")
rating = data["Rating"] >4.0
print(rating)

print("\n\n")
sort_data = data.sort_values("Salary",ascending = False)
print(sort_data)
