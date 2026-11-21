#61. Write a class decorator that adds a greet() method to any class it decorates.


def decorator (cls):
    def greet(self):
        print("Hello everyone! from",self.__class__.__name__)

    cls.greet = greet
    return cls


@decorator
class Student:
    def __init__(self):
        pass
@decorator
class Employee:
    def __init__(self):
        pass
s = Student()
e = Employee()
s.greet()
e.greet()



