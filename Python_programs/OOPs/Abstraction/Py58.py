"""
Implement an abstract class Employee with attributes name and salary, and abstract method calculate_bonus().
Subclasses Manager and Developer should implement their own bonus calculation logic.
"""

from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_bonus(self,bonus):
        pass

class Manager(Employee):
    def calculate_bonus(self,bonus):
        bonus += self.salary
        print(f"\nName: {self.name}\nSalary: {self.salary}\nBonus: {bonus}\n")

class Developer(Employee):
    def calculate_bonus(self,bonus):
        bonus += self.salary
        print(f"\nName: {self.name}\nSalary: {self.salary}\nBonus: {bonus}\n")

m = Manager("John",20000)
d = Developer("Alice",10020)
m.calculate_bonus(20000)
d.calculate_bonus(20000)


