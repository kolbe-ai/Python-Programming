"""
Write a program to create a dictionary of student names and marks,
then print students who scored above 75.
"""

student = {}
num = int(input("Enter the number of student: " ))
for i in range(num):
    name = input(f"Enter the student name {i+1} : ")
    mark = float(input(f"Enter the student mark {i+1} : "))
    student[name] = mark

"""avg = 0
for i in student.values():
    avg += i
avg = avg/num"""
print("\n|--Students above average --|\n")
for keys,values in student.items():
    if 75<values:
        print(f"Student: {keys}\nMark: {values}\n")
