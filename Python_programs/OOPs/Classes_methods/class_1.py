"""
Create a class Student with class variable college_name, instance variables name and marks, and a method returning the grade.
Create 2 objects and show that changing the class variable affects both.
"""

class Student:
  college_name = ""
  def __init__(self,name,mark):
    self.name = name
    self.mark = mark
    self.grade = ''
  def cal_grade(self):
    if self.mark>=90:
        return 'A'
    elif self.mark>=80:
        return 'B'
    elif self.mark>=70:
        return 'C'
    elif self.mark>=60:
        return 'D'
    elif self.mark>=50:
        return 'E'
    else:
        return 'F'
  def display(self):
    self.grade = self.cal_grade()
    print(f"Name: {self.name}\nMark: {self.mark}\nGrade: {self.grade}\nCollege: {self.college_name}\n\n")


s1 = Student("Arun",100)
s1.college_name = "IIT Madras"

s2 = Student("Ravi",89)
s2.college_name = "IIT Pune"

s1.display()
s2.display()
