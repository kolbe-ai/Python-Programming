"""
Build AnimalFactory that returns Dog, Cat, or Bird from a user string and calls speak() on each.
"""

class Dog:
    def speak(self):
        print("Dog: Bwok Bwok Bwok !!!")

class Cat:
    def speak(self):
        print("Cat: Meow Meow Meow...")
class Bird:
    def speak(self):
        print("Bird: Chww Chww Chww~~~~")

class AnimalFactor:
    def speaking(self,user):
        match user.lower():
            case "dog":
                return Dog()
            case "cat":
                return Cat()
            case "bird":
                return Bird()


n = input("Enter the animal: ")
a = AnimalFactor()
animal = a.speaking(n)
animal.speak()