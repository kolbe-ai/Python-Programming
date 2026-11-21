"""
Create a ComplexNumber class with real and imaginary attributes.
Overload + to add two complex numbers and == to compare them, and demonstrate both with examples.
"""

class ComplexNumber:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        return ComplexNumber(self.real+other.real, self.img+other.img)
    def __eq__(self,other):
        return self.real == other.real and self.img == other.img
    def display(self):
        print(f"{self.real} + {self.img}i")

c1= ComplexNumber(2,3)
c2= ComplexNumber(3,4)
c3 = ComplexNumber(2,3)
print(f"C1: ",end="")
c1.display()
print(f"C2: ",end="")
c2.display()

c4 = c1+c2

print(f"Sum of complex is: ",end="")
c2.display()
print(f"\nIs c1 and c2 same: ",c1== c2)
print(f"Is c1 and c3 same: ",c1== c3)