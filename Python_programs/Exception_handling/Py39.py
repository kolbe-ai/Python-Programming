"""
Create a calculator that handles ZeroDivisionError, ValueError, and
any unexpected error using a generic except block
"""
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    op = input("Enter + - * / ^ : ")
    result = 0
    match(op):
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case '^':
            result = num1 ** num2
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Invalid number")
except Exception as e:
    print(f"Error occured\nError details: {e}")
