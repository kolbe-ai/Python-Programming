"""
Implement a Student Management System using the MVC pattern:
Model: Student data (name, roll number, marks).
View: Display student details.
Controller: Handle input and update model/view.
"""

class Model:
    def __init__(self,name,no,marks):
        self.name = name
        self.no = no
        self.marks = marks
    def update(self,mark):
        #new mark
        self.marks = mark

