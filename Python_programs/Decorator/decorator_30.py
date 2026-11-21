"""
30. Create a Student class with name and marks. Overload the >
operator to compare two students based on their marks. Demonstrate
the comparison using suitable objects.
"""


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __gt__(self,other):
        return (self.marks > other.marks)

s1 = Student("Rohit",100)
s2 = Student("Ravi",99)
print(s1>s2)