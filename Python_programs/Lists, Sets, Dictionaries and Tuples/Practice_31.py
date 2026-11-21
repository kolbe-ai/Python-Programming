"""
31. (Student Marks Analyzer) Read marks for n students and
display the highest, lowest and average marks, plus the number of students who scored above the average.
"""

print("!----\tStudent Marks INPUT \t----!\n")

n = int(input("Enter the number of student: "))
mark = []
for i in range(n):
    m = int(input(f"Enter the mark of the student {i+1} : "))
    mark.append(m)

print("\n\n!----\tStudent Marks Analyzer \t----!\n")
max_mark = max(mark)
min_mark = min(mark)
sum_mark = sum(mark)
avg_mark = sum_mark/ len(mark)
print(f"Maximum : {max_mark}\nMinimum mark: {min_mark}\nAverage mark: {avg_mark}\n")

count = 0
print("\n\n!----\tStudent Marks Analyzer \t----!\n")
for i in mark:
    if i>avg_mark:
        count += 1
        print("Above average: ",i)

print("\n\nNumber of student who scored above average is: ",count)