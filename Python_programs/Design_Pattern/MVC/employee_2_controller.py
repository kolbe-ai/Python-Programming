"""
Develop a simple Employee Management System using MVC
architecture. Store employee ID, name and salary in the Model.
Implement suitable methods in the View to display employee
information and use the Controller to add and display employee details.
"""


from employee_2_model import model
from employee_2_view import view

class Controller:
    def __init__(self):
        self.model = model()
        self.view = view()

    def controller_employee(self):
        #printing the current employee
        current_employee = self.model.get_employee()
        self.view.view_all(current_employee)

        #adding employee
        id = int(input("Enter the employee id: "))
        name = input("Enter the employee name: ")
        salary = float(input("Enter the employee salary: "))
        self.model.add_employee(id,name,salary)
        current_employee = self.model.get_employee()
        self.view.view_all(current_employee)

if __name__ == "__main__":
    x = Controller()
    x.controller_employee()