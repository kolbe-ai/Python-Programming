#Create a class Rectangle with a constructor, area(), and perimeter().

class Rectangle:
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    def area(self):
        return self.length * self.bredth
    def perimeter(self):
        return 2*(self.length + self.bredth)
    def display(self):
        print(f"Area: {self.area()}\nPerimeter: {self.perimeter()}")

r = Rectangle(20,10)
r.area()
r.perimeter()
r.display()