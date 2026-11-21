"""
Write a class decorator that adds a new method greet() to any class it decorates.
"""

def decorator(cls):
    def greeting(self):
        print("Hello to the world from ",self.__class__.__name__)
    cls.greet = greeting    #injecting the method
    return cls


@decorator
class Greet:
    def __init__(self,message):
        print(message)

g = Greet("Hello")
g.greet()
