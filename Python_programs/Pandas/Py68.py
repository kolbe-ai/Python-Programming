"""
 You are given the following dataset of students and their exam scores:
Name	Class	Subject	Marks
Anu		10		Maths	78
Ravi		10		Science	85
Meera	9		Maths	92
John		9		English	67
Asha		10		English	74
Ramesh	9		Science	81
Perform the following tasks using Pandas:
Create a DataFrame from the given data.
Add a new column Result:
If Marks ≥ 75 → "Pass"
Else → "Fail"
   c. Add another column Grade using a user-defined function:
Marks ≥ 90 → "A+"
80–89 → "A"
70–79 → "B"
Else → "C"
   d. Group the data by Class and find the average marks for each class.
   e. Use boolean indexing to display only the students who scored above 80
marks.
    f. Sort the DataFrame by Marks in descending order.
"""

import pandas as pd

#Create a DataFrame from the given data.
data = {"Name" : ["Anu","Ravi","Meera","John","Asha","Ramesh"],
        "Class" : [10,10,9,9,10,9],
        "Subject" : ["Maths","Science","Maths","English","English","Science"],
        "Marks": [78,85,92,67,74,81]}
students = pd.DataFrame(data)
print(students)

#Add a new column Result: If Marks ≥ 75 → "Pass" Else → "Fail"
res = []
for i in students["Marks"]:
    if i >=75:
        res.append("Pass")
    else:
        res.append("Fail")
students["Result"] = res
print("\n\nWith result:\n",students)

# c. Add another column Grade using a user-defined function: Marks ≥ 90 → "A+" , 80–89 → "A" , 70–79 → "B" , Else → "C"
grd = []
for i in students["Marks"]:
    if (i>=90):
        grd.append("A+")
    elif (i<= 89 & i>= 80):
        grd.append("A")
    elif (i<= 79 & i>= 70):
        grd.append("B")
    else:
        grd.append("C")

#d. Group the data by Class and find the average marks for each class.
group_data = students.groupby("Class")["Marks"].mean()
print("\n\nThe grouped data: \n",group_data)


#e. Use boolean indexing to display only the students who scored above 80 marks.
print("\n\nThe student who scored about 80 marks: \n",(students[students["Marks"]>80]))

#f. Sort the DataFrame by Marks in descending order.
sorted_data = students.sort_values("Marks",ascending = False)
print("\n\nSorted data: \n",sorted_data)