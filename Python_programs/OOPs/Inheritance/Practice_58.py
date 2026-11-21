"""
58. Create an abstract class Employee (name, salary) with an abstract method calculate_bonus().
Implement Manager and Developer subclasses, each with its own bonus logic.
"""

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_bonus(self):
        pass
    def display(self):
        print(f"\n\nName: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Bonus: {self.calculate_bonus()}")
        print(f"Full salary: {self.calculate_bonus() + self.salary}")

class Manager (Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_bonus(self):
        return 0.15*self.salary
class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_bonus(self):
        return 0.10*self.salary

m = Manager("Ravi",452242)
m.display()
m.calculate_bonus()
m.display()

c = Developer("Rohan",43456)
c.display()
c.calculate_bonus()
c.display()