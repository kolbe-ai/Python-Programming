"""
(Abstraction + Inheritance) [PDF Q58] Create an abstract Employee with abstract calculate_bonus().
Implement Manager (20%) and Developer (10%).
"""

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_bonus(self,salary,bonus):
        pass

class Manager(Employee):
    def calculate_bonus(self,salary,bonus):
        salary *= bonus/100
        return salary
class Developer(Employee):
    def calculate_bonus(self,salary,bonus):
        salary *= bonus/100
        return salary

m = Manager()
print("Manager: ",m.calculate_bonus(20000,20))
d = Developer()
print("Developer: ",d.calculate_bonus(2000000,10))