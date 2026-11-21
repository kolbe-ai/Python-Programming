"""
Create a base class Employee with attributes name and salary and a method display_details().
Derive two subclasses: Manager with an extra attribute department and Developer with an attribute programming_language.
Both subclasses should override display_details() to show their details.
Write a program to create objects of both classes and display their information using method overriding.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name,salary)
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}\nDepartment: {self.department} \nSalary: {self.salary}\n")


class Devoloper(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language
    def display_details(self):
        print(f"Name: {self.name}\nProgramming language: {self.language} \nSalary: {self.salary}\n")


m1 = Manager("John",200000,"Finance")
d1 = Devoloper("Bob",2000000,"C programing")

m1.display_details()
d1.display_details()


