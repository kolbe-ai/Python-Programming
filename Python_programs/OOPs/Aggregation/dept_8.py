"""
8. Create Department and Employee classes to demonstrate aggregation.
A Department should contain references to multiple Employee objects.
Demonstrate that employees can exist independently even after the
Department object is deleted
"""

class Department:
    def __init__(self,d_name):
        self.d_name = d_name

class Employee:
    def __init__(self,e_name,d_name):
        self.e_name = e_name
        self.d_name = d_name
    def display(self):
        print(f"Name: {self.e_name}\tDepartment: {self.d_name.d_name}")



dept = Department("Computer")
e1 = Employee("Ravi",dept)
e2 = Employee("Rahul",dept)
e3 = Employee("John",dept)

print(f"\n\nThe employee:")
e1.display()
e2.display()
e3.display()

#deleting dept
del dept

#printing again
print(f"\n\nThe employee:")
e1.display()
e2.display()
e3.display()
