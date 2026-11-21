"""
27. Create a class decorator that adds a greet() method to any class it
decorates. Apply the decorator to a class containing student or
employee details and demonstrate the newly added method.
"""

def decorator(func):
    def wrapper(self):
        print("Hello how are you!")
        return func(self)
    return wrapper

class Student:
    def __init__(self,message):
        self.message = message
    @decorator
    def show(self):
        print("Hello")

s1 = Student("Raju")
s1.show()