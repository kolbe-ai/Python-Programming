"""
Write a divide program that handles ZeroDivisionError, ValueError, and a generic Exception, and uses else and finally. State what prints in each case.
"""

try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    res = n1/n2
    print("Division: ",res)

except(ZeroDivisionError):
    print("Cannot divide by zero")
except(ValueError):
    print("It should be numeber")
except Exception:
    print("Error occured")
else:
    print("No error occured")
finally:
    print("Process completed")