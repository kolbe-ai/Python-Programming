"""
Create a class ComplexNumber with attributes real and imaginary.
Overload the + operator to add two complex numbers. Overload the == operator to check if two complex numbers are equal.
Demonstrate these operations using suitable examples.
"""

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self,other):
        added_real = self.real+other.real
        added_img = self.imaginary + other.imaginary
        return ComplexNumber(added_real,added_img)
    def __eq__(self,other):
        return self.real == other.real and self.imaginary == other.imaginary




    def display(self):
        print(f"{self.real} + {self.imaginary} i")


r1 = int(input("Enter the real number: "))
i1 = int(input("Enter the imaginary number: "))
r2 = int(input("Enter the real number: "))
i2 = int(input("Enter the imaginary number: "))

c1 = ComplexNumber(r1,i1)         #5 + 3i
c2 = ComplexNumber(r2,i2)         #6 + 7i
c3 = c1+c2
print("\nSum: ")
c3.display()
print(f"\nIs these complex number equal: {c1 == c2}")
