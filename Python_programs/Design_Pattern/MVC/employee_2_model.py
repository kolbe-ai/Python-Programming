"""
Develop a simple Employee Management System using MVC
architecture. Store employee ID, name and salary in the Model.
Implement suitable methods in the View to display employee
information and use the Controller to add and display employee details.
"""

class model:
    def __init__(self):
        self.employee = {101:{"name" : "Rohit","salary": 987654321}}
    def add_employee(self,empid,ename,salary):
        self.employee[empid] = {"name": ename,"salary": salary}
    def get_employee(self):
        return self.employee
