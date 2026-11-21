"""
29. Create New_calc.py with functions for addition, subtraction, multiplication and division.
In a separate file, build a menu-driven program that imports and uses these functions.
"""

import New_calc as calc

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
op = input("Enter the operation: ")
match(op):
    case '+':
        res = calc.add(num1,num2)
        print("Result = ",res)
    case '-':
        res = calc.sub(num1,num2)
        print("Result = ",res)
    case '*':
        res = calc.mul(num1,num2)
        print("Result = ",res)
    case '/':
        res = calc.div(num1,num2)
        print("Result = ",res)
    case '%':
        res = calc.rem(num1,num2)
        print("Result = ",res)


