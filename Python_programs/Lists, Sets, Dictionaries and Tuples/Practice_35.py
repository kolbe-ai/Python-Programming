#35. Create a dictionary of student names and marks, then print the students who scored above 75.

student = {"Ravi": 100,"Rajiv": 98,"Rahul": 97,"Rohan":95}
for i,j in student.items():
    if j> 75:
        print(i,j)