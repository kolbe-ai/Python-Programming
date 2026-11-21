"""
Implement a Student Management System using the MVC pattern:
● Model: Student data (name, roll number, marks).
● View: Display student details.
● Controller: Handle input and update model/view.
"""

class v_view:
    def view_all(self,student):
        for rollno, name in student.items():
            print(f"Student rollno: {rollno}\t Student name: {name}")


