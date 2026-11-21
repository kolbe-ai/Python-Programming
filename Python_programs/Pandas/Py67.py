"""
You are given the following employee data:
Name	Department	Salary
John			HR		45000
Alice		IT		55000
Bob			HR		40000
David		IT		60000
Emma	   Finance		50000
Perform the following tasks using Pandas:
Create a DataFrame from the above data.
Add a new column Bonus which is 10% of the salary.
Group the data by Department and find the average salary in each department.
Add another column Category based on a function:
    If Salary >= 50000 → "High"
    Else → "Low"
Display only those employees whose salary is greater than 45000 (use boolean indexing).
"""

import pandas as pd

data = {"Name": ["John","Alice","Bob","David","Emma"],
        "Department" : ["HR","IT","HR","IT","Finance"],
        "Salary" : [45000,55000,40000,60000,50000]}
df = pd.DataFrame(data)
df["Bonus"] = df["Salary"]/10
print(df)
grouped_data = df.groupby('Department')['Salary'].mean()
print("\nGrouped data is: \n",grouped_data)

#adding low and high
cat = []
for i in df["Salary"]:
    if (i<=50000):
        cat.append("Low")
    else:
        cat.append("High")
df["Category"] = cat
print("\nNew data: \n",df)

#Display only those employees whose salary is greater than 45000 (use boolean indexing).
print("\n\nEmployee whose salary is greater than 45000: \n",df[df["Salary"] > 45000])