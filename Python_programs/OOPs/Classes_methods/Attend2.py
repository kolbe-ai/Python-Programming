"""
Question 2: Rectangle
Create a Rectangle class with the following:
 Attributes: length, breadth
 Methods:
o area()
o perimeter()

Task:
 Create two Rectangle objects with different dimensions.
 Call both the area() and perimeter() methods for each object.
 Display the calculated area and perimeter.
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breath = breadth
    def area(self):
        area = self.length * self.breath
        print(f"\nArea of the rectangle is: {area}")
    def perimeter(self):
        perimeter = 2*(self.length * self.breath)
        print(f"Perimeter of the rectangle is: {perimeter}")

length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
r1 = Rectangle(length,breadth)

length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
r2 = Rectangle(length,breadth)

r1.area()
r1.perimeter()

r2.area()
r2.perimeter()