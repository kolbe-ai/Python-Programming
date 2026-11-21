"""Create a base class Employee (name, salary, display_details()) with two subclasses:
Manager (extra attribute department) and Developer (extra attribute programming_language).
Both override display(). Create objects of each and display their details.
"""

class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"\nName: {self.name}\nSalary: {self.salary}\n\n")

class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept = dept
    def display(self):
        print(f"\nName: {self.name}\nDepartment: {self.dept}\nSalary: {self.salary}")
class Developer(Employee):
    def __init__(self,name,salary,*lang):
        super().__init__(name,salary)
        self.lang = lang
    def display(self):
        print(f"\nName: {self.name}\nLanguage: {self.lang}\nSalary: {self.salary}")

m = Manager("Ravi",8756789,"Business")
d = Developer("Rahul",98765678,"C programing","Java","Python","Assemply","SQL")
m.display()
d.display()