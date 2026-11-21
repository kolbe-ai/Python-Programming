"""
Develop a simple Employee Management System using MVC
architecture. Store employee ID, name and salary in the Model.
Implement suitable methods in the View to display employee
information and use the Controller to add and display employee details.
"""

class view:
    def view_all(self,employee):
        print(f"\nThe details of the employee is:")
        for id,details in employee.items():
            print(f"ID: {id}\tName: {details["name"]}\tSalary: {details["salary"]}")

