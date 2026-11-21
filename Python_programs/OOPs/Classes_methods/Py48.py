"""
Create a class Circle with a constructor to initialize radius and methods to calculate area and circumference.
Return the results and display them.
"""

class Circle:
    area = 0.0
    circum = 0.0
    def __init__(self,radius):
        self.radius = radius
    def area_c(self):
        self.area = 3.14*pow(self.radius,2)
    def circum_c(self):
        self.circum = 2*3.14*radius
    def display(self):
        print("Circle radius: %.2f\nCircumference: %.2f\nArea: %.2f\n\n"%(self.radius,self.circum,self.area))


radius = float(input("Enter the radius of the circle: "))
c1 = Circle(radius)
c1.circum_c()
c1.area_c()
c1.display()


