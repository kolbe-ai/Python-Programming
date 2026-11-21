"""
18. You are given the following employee data:
Name Department Salary
John HR 45000
Alice IT 55000
Bob HR 40000
David IT 60000
Emma Finance 50000
Perform the following tasks using Pandas:
a. Create a DataFrame from the above data.
b. Add a new column Bonus which is 10% of the salary.
c. Group the data by Department and find the average salary in each
department.
d. Add another column Category based on a function:
i. If Salary >= 50000 → "High"
ii. Else → "Low"
e. Display only those employees whose salary is greater than 45000
(use boolean indexing).
"""

import pandas as pd

data = {"Name" : ["John","Alice","Bob","David","Emma"],
        "Department": ["HR","IT","HR","IT","Finance"],
        "Salary": [45000,55000,40000,60000,50000]}
df = pd.DataFrame(data)

#printing the dataframe
print(df)

#adding column
print("\nAfter adding bonus:")
df["Bonus"] = df["Salary"]*.10
print(df)

#after grouping
print("\nGrouped data: ")
dept = df.groupby("Department")["Salary"].mean()
print(dept)

#adding cateogry
cat = []
for i in df["Salary"]:
        if(i>=50000):
                cat.append("High")
        else:
                cat.append("Low")
df["Category"] = cat
print(df)

#whose salary is greater than 45000
print("\n\nSalary is greater than 45000:")
print(df[df["Salary"]>45000])