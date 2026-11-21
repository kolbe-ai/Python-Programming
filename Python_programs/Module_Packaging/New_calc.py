"""
29. Create New_calc.py with functions for addition, subtraction, multiplication and division.
In a separate file, build a menu-driven program that imports and uses these functions.
"""


def add(num1, num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if (num2 == 0):
        return None
    else:
        return num1/num2
def rem(num1,num2):
    return num1%num2