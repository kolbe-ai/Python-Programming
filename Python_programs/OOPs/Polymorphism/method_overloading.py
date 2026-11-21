"""
Write area(a, b=None) that gives the area of a square if one value is passed, or a rectangle if two are.
"""

def area(a,b=None):
    if b == None:
        return a*a
    return a*b

square = area(10)
rectangle = area(10,20)
print("Area of square: ",square)
print("Area of rectangle: ",rectangle)