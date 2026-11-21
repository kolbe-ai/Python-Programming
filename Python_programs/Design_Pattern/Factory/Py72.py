Implement a ShapeFactory that creates different shapes (Circle, Square, Rectangle) based on user input.
Demonstrate polymorphism by calling the area() method on each shape.
"""
class Circle:
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return 3.14*self.radius**2
class Square:
  def __init__(self,side):
    self.side = side
  def area(self):
    return self.side**2
class Rectangle:
  def __init__(self,length,bredth):
    self.length = length
    self.bredth = bredth
  def area(self):
    return self.length * self.bredth

def ShapeFactory(shape):
  shape = shape.lower()
  if shape == 'circle':
    c = Circle(10)
    area = c.area()
  if shape == 'square':
    s = Square(10)
    area = s.area()
  if shape == 'rectangle':
    r = Rectangle(10,20)
    area = r.area()
  print("Area is: ",end = "")
  print(area)

shape = input("Enter the shape: ")
ShapeFactory(shape)