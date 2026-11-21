"""
Create an abstract class. Shape with an abstract method area() and to display the result .
Implement subclasses Circle and Rectangle to calculate respective areas.
"""

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def display(self):
        print(f"The area of {self.__class__.__name__} is {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

cir = Circle(10)
rect = Rectangle(20,20)

cir.display()
rect.display()