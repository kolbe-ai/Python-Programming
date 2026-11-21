"""
Implement a Student Management System using the MVC pattern:
● Model: Student data (name, roll number, marks).
● View: Display student details.
● Controller: Handle input and update model/view.
"""

class s_model:
    def __init__(self):
        self.student = {101: "Rahul",102: "Ravi"}
    def add_item(self,rollno,std):
        self.student[rollno] = std
    def current_item(self):
        return self.student


