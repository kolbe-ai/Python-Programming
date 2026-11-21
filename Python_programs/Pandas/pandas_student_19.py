"""
19. You are given the following dataset of students and their exam
scores:
Name Class Subject Marks
Anu 10 Maths 78
Ravi 10 Science 85
Meera 9 Maths 92
John 9 English 67
Asha 10 English 74
Ramesh 9 Science 81
Perform the following tasks using Pandas:
a. Create a DataFrame from the given data.
b. Add a new column Result:
○ If Marks ≥ 75 → "Pass"
○ Else → "Fail"
c. Add another column Grade using a user-defined function:
Marks ≥ 90 → "A+"
70–79 → "B"
Else → "C"
d. Group the data by Class and find the average marks for each class.
e. Use boolean indexing to display only the students who scored above 80
marks.
f. Sort the DataFrame by Marks in descending order.
"""

import pandas as pd

data = {"Name": ["Anu","Ravi","Meera","John","Asha","Ramesh"],"Class" : [10,10,9,9,10,9], "Subject": ["Maths","Science","Maths","English","English","Science"], "Marks": [78,85,92,67,74,81]}
df = pd.DataFrame(data)
print(df)


##b
res = []
for i in df["Marks"]:
    if(i >= 75):
        res.append("Pass")
    else:
        res.append("Failed")
print("\n\nNew Data Set is: ")
df["Result"] = res
print(df)

#c
grade = []
for i in df["Marks"]:
    if i>= 90:
        grade.append("A+")
    elif i<= 89 and i>=80:
        grade.append("A")
    elif i<= 79 and i>= 70:
        grade.append("B")
    else:
        grade.append("C")
df["Grade"] = grade
print("\n\nGrade Databse is: ")
print(df)

#d. Group the data by Class and find the average marks for each class.
grouped = df.groupby("Class")["Marks"].mean()
print(f"\n\nGrouped Data is: {grouped}")

#e. Use boolean indexing to display only the students who scored above 80
print("The marks of students greater than 80 is: ")
print(df[df["Marks"]>80])

#f. Sort the DataFrame by Marks in descending order.
print("\n\nSorted data by mark descending order")
desc = df.sort_values("Marks",ascending = False)
print(desc)