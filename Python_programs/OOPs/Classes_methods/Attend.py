"""
Create an Employee class with the following:
 Attributes: emp_id, name, basic_salary
 Method:
o calculate_salary() that calculates the gross salary by adding 20% HRA
and 10% DA to the basic salary.

Task:
 Create at least two Employee objects.
 Call the calculate_salary() method for each object.
 Display the employee details along with the gross salary.
"""

class Employee:
    def __init__(self,emp_id,name,basic_sal):
        self.emp_id = emp_id
        self.name = name
        self.basic_sal = basic_sal
    def calculate_salary(self):
        self.basic_sal += self.basic_sal* (20/100)
    def display(self):
        print(f"\nThe employee id: {self.emp_id}\nThe employee name: {self.name}\nThe basic salary: {self.basic_sal}\n")


emp_id = int(input("\nEnter the emp id: "))
name = input("Enter the employee name: ")
basic_sal = float(input("Enter the salary: "))
emp1 = Employee(emp_id,name,basic_sal)

emp_id = int(input("Enter the emp id: "))
name = input("Enter the employee name: ")
basic_sal = float(input("Enter the salary: "))
emp2 = Employee(emp_id,name,basic_sal)

emp1.calculate_salary()
emp1.display()
emp2.calculate_salary()
emp2.display()