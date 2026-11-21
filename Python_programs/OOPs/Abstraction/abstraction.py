"""
(Abstraction: Abstract Class) [PDF Q56] Create an abstract class Animal with abstract sound(), then implement Cat and Cow.
What happens if you try to create Animal() directly?
"""

from abc import ABC,abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass

class Dog(Animal):
  def __init__(self):
    print("Hello from dog")

class Cat(Animal):
  def __init__(self):
    print("Hello from cat")

c = Cat()
d = Dog()
