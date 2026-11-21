"""
29. Create a class ComplexNumber with attributes real and imaginary.
Overload the + operator to add two complex numbers. Overload the ==
operator to check if two complex numbers are equal. Demonstrate
these operations using suitable examples
"""

class ComplexNumber:
    def __init__(self,real,complex):
        self.real = real
        self.complex = complex
    def __add__(self,other):
        return ComplexNumber(self.real+other.real, self.complex + other.complex)

    def __eq__(self,other):
        return (self.real == other.real and self.complex == other.complex)
    def display(self):
        print(f"Imaginary number is: {self.real} + {self.complex}i")


c1 = ComplexNumber(2,3)
c2 = ComplexNumber(4,5)

c3 = c1+c2
c3.display()

c4 = ComplexNumber(4,5)
print(c2 == c4)
print(c2 == c3)
