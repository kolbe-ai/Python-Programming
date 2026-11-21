"""
28. Write a decorator that logs the name of a function and its arguments
whenever the function is called. Apply it to at least two suitable
functions and demonstrate the output
"""

def decorator(func):
    def wrapper(*args):
        print("Func: ",func.__name__,"\t Argument: ",args)
        return func(*args)
    return wrapper

@decorator
def add(num1,num2):
    return num1+num2
@decorator
def display(name):
    print(name)

display("Ravi")
print(add(1,2))

