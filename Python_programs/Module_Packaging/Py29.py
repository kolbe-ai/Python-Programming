"""
Write a program that defines functions for addition, subtraction,
multiplication, and division in a Calc.py file. In another file, create a
menu-driven application and import the function as needed.
"""
import Calc
choice = int(input("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\n\nEnter your choice: "))
if choice in [1,2,3,4]:
    match(choice):
        case 1:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            result = Calc.add(num1,num2)
            print(result)
        case 2:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            result = Calc.sub(num1, num2)
            print(result)
        case 3:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            result = Calc.mul(num1, num2)
            print(result)
        case 4:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            result = Calc.div(num1, num2)
            print(result)
else:
    print("Invalid choice")
