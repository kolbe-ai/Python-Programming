#39. Build a calculator that handles ZeroDivisionError, ValueError and any other unexpected error with a generic except block.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    op = input("Enter the operator: ")
    match(op):
        case '+':
            print("\nResult: ",(num1+num2))
        case '-':
            print("\nResult: ",(num1-num2))
        case '*':
            print("\nResult: ",(num1*num2))
        case '/':
            if (num2 == 0):
                raise ZeroDivisionError
            print("\nResult: ",(num1/num2))
except ValueError as e:
    print("Error: ",e)
except ZeroDivisionError as e1:
    print("Error: ",e1)
except Exception as e:
    print("Error: ",e)
else:
    print("\nCompleted with no error!")
finally:
    print("Process completed")