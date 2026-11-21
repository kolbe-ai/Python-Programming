"""
Create a module called shapes.py that contains functions to calculate
the area of a circle, rectangle, and triangle. Import the module in your
main program and use the functions.
"""
import Shapes
while(True):
    choice = int(input("Enter 1 for circle\nEnter 2 for rectangle \nEnter 3 for square\nEnter 4 to exit\n\nEnter your choice: "))
    if choice == 1:
        radius = float(input("Enter radius: "))
        result = Shapes.circle(radius)
        print(result)
    elif choice == 2:
        l = int(input("Enter length: "))
        b = int(input("Enter breadth: "))
        result = Shapes.rectangle(l,b)
        print(result)
    elif choice == 3:
        side  = int(input("Enter side: "))
        result = Shapes.square(side)
        print(result)
    elif choice == 4:
        break
    else:
        print("Invalid choice")