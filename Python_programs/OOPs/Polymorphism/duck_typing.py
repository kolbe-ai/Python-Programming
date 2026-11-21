"""
Demonstrate duck typing with classes Dog, Robot, Duck that each have speak(), plus a function make_it_speak(obj).
"""

class Dog:
    def speak(self):
        print("Bowh bowh bowh")
class Robot:
    def speak(self):
        print("Grh Grh Grh ")
class Duck:
    def speak(self):
        print("Quack! Quack! Quack!")

def make_it_speak(obj):
    obj.speak()

d = Dog()
r = Robot()
duck = Duck()
make_it_speak(d)
make_it_speak(r)
make_it_speak(duck)