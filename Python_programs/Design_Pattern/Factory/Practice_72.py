"""
72. (Factory) Implement a ShapeFactory that creates Circle, Square or Rectangle objects based on user input,
and demonstrate polymorphism by calling area() on each.
"""

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 22/7 * pow(self.radius,2)
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
class Rectangle(Shape):
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    def area(self):
        return self.length*self.bredth

class ShapeFactory:
    def __init__(self,shape):
        self.shape = shape.lower()
    def factory(self):
        match(self.shape):
            case "circle":
                return Circle(7)
            case "square":
                return Square(10)
            case "rectangle":
                return Rectangle(10,20)
            case _:
                return None


user_input = input("Enter the shape (circle,square,rectangle): ")
factory_instance = ShapeFactory(user_input)
shape_instance = factory_instance.factory()
print("Area is: ",shape_instance.area())



