"""
51. Write an add() function that can add two numbers, add three numbers, or concatenate two strings.
Use default arguments to simulate method overloading.
"""


def add(a,b,c=None):
    if c is None:
        return a+b
    else:
        return a+b+c

print("Sum of 2 numbers are: ",add(1,2))
print("Sum of 3 numbers are: ",add(1,2,3))
print("Sum of 2 strings are: ",add("hello ","world"))