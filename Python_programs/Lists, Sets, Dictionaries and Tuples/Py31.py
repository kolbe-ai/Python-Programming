"""
Student Marks Analyzer
Write a Python program to:
● Input marks of n students.
● Display the highest, lowest, and average marks.
● Count the number of students who scored above the average.
Concepts: List input, max(), min(), sum(), loops, conditionals.
"""

num = int(input("Enter the number of students: "))
student = []
mark = []
for i in range (num):
    sd = int(input("Enter the student ID: "))
    marks = float(input("Enter the student mark: "))
    student.append(sd)
    mark.append(marks)
min_mark = min(mark)
max_mark = max(mark)
avg_mark = sum(mark)/num
count = 0
for i in mark:
    if i > avg_mark:
        count += 1
print(f"Min mark is: {min_mark}")
print(f"Max mark is: {max_mark}")
print(f"Avg mark is: {avg_mark}")
print(f"Number of student above average mark is: {count}")
