"""
68. Using the given student data
Name Class Subject Marks
Anu 10 Maths 78
Ravi 10 Science 85
Meera 9 Maths 92
John 9 English 67
Asha 10 English 74
Ramesh 9 Science 81
(a) create a DataFrame,
(b) add Result (“Pass” if Marks ≥ 75, else “Fail”),
(c) add Grade with a user-defined function (≥90 “A+”, 80-89 “A”, 70-79 “B”, else “C”),
(d) group by Class and find the average marks,
(e) use boolean indexing to show students above 80,
(f) sort by Marks in descending order.
"""

import pandas as pd

#a
data = {"Name": ["Anu","Ravi","Meera","John","Asha","Ramesh"] , "Class": [10,10,9,9,10,9], "Subject": ["Maths","Science","Maths","English","English","Science"],"Marks": [78,85,92,67,74,81]}
df = pd.DataFrame(data)
print("\n\nData is: \n",df)

#b
result =[]
for i in data["Marks"]:
    if (i>=75):
        result.append("Pass")
    else:
        result.append("Fail")

df["Result"] = result
print("\n\nAdded Result is: \n",df)

#c
def grade_(mark):
    if (mark>=90):
        return 'A'
    elif (mark>=80):
        return 'B'
    elif (mark>=70):
        return 'C'
    elif (mark>=60):
        return 'D'
    elif(mark>=50):
        return 'E'
    else:
        return 'F'
grade = []
for i in data["Marks"]:
    c = grade_(i)
    grade.append(c)

df["Grade"] = grade
print("\n\nWith Grade is: \n",df)


#(d) group by Class and find the average marks,
grouped = df.groupby("Class")["Marks"].mean()
print("\n\nGrouped data is: \n",grouped)


#(e) use boolean indexing to show students above 80,
indexing = df[df["Marks"] > 80]
print("\n\nStudent above 80 is: \n",indexing)


#(f) sort by Marks in descending order.
ordered = df.sort_values("Marks",ascending=False)
print("\n\nOrdered is: \n",ordered)
print("\n\nOrdered is: \n",ordered)