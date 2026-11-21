"""
Implement a Student Management System using the MVC pattern:
Model: Student data (name, roll number, marks).
View: Display student details.
Controller: Handle input and update model/view.
"""

class View:
    def display(name,no,marks):
        print(f"\nName: {name}\nRoll no: {no}\nMarks: {marks}\n")
