"""
#(Decorator: Class Decorator) [PDF Q61] Write a class decorator @add_hello that adds a hello() method to any class.
"""


def add_hello(cls):
    def hello(*args):
        print("Hello from decorator")
        
    cls.hello = hello
    return cls


@add_hello
class Car:
    def __init__(self):
        print("Car starts")


c = Car()
c.hello()
