# 30. Create shapes.py with functions for the area of a circle, rectangle and triangle. Import it in a main program and use the functions.

import New_shapes as shape

sh = input("Enter the shape: ")
if (sh.lower() == 'triangle'):
    bredth = int(input("Enter the bredth: "))
    height = int(input("Enter the height: "))
    res = shape.triangle(bredth,height)
    print("Area: ",res)
elif (sh.lower() == 'rectangle'):
    bredth = int(input("Enter the bredth: "))
    length = int(input("Enter the length: "))
    res = shape.rectangle(length,bredth)
    print("Area: ",res)
elif (sh.lower() == 'circle'):
    radius = float(input("Enter the radius: "))
    res = shape.circle(radius)
    print("Area: ",res)
else:
    print("Invalid shape")