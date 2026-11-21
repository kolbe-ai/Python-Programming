"""
56. Create an abstract class Shape with an abstract method area() and a way to display the result.
Implement Circle and Rectangle subclasses that calculate their own areas.

from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        print("Area is: ",(22/7*radius*radius))
class Rectangle(Shape):
    def area(self,length,bredth):
        print("Area is: ",(length*bredth))

c = Circle()
c.area(7)

r = Rectangle()
r.area(10,20)

"""

"""
56. Create an abstract class Shape with an abstract method area() and a way to display the result.
Implement Circle and Rectangle subclasses that calculate their own areas.
"""

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def display(self):
        print("Area is: ",self.area())

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 22/7*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    def area(self):
        return self.length*self.bredth

c = Circle(7)
c.display()

r = Rectangle(10,20)
r.display()