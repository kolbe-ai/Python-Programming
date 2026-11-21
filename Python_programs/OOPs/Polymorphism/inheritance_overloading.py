Create base class Vehicle and subclasses Car and Bike that override display(). Use super().__init__() in at least one.
"""

class Vehicle:
    def __init__(self,vehicle):
        self.vehicle = vehicle
    def display(self):
        print("Vehicle type: ",self.vehicle)

class Car(Vehicle):
    def __init__(self):
        super().__init__("Car")
    def display(self):
        super().display()
        print("CC: 2500cc\n")

class Bike(Vehicle):
    def __init__(self):
        super().__init__("Bike")
    def display(self):
        print("\nVehicle: Bike\nCC: 650")

c = Car()
b = Bike()
c.display()
b.display()