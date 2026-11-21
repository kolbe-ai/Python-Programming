"""
48. Create a Circle class whose constructor takes the radius, with methods to calculate area and circumference.
Return the results and display them.
"""

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        print("\n\nThe area of the circle is: ",(self.radius*self.radius*22/7))
    def calculate_circumference(self):
        print("\nThe circumference of the circle is: ",(2*22/7*self.radius))

c1 = Circle(7)
c1.calculate_area()
c1.calculate_circumference()