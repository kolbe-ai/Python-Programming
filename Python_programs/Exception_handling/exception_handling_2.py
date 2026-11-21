"""
Create a custom exception InvalidAgeError raised when age is below 0 or above 120. Use it in a function and catch it in a try/except/else/finally.
"""

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age<=0 or age>120:
        raise InvalidAgeError("Invalid error")
    return age

try:
    age = int(input("Enter the age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error: ",e)
else:
    print("Valid age")
finally:
    print("Process completed")
