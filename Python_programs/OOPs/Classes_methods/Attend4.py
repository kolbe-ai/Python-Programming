"""
Question 4: Car Showroom
Create a Car class with the following:
 Attributes: brand, model, price
 Method:
o display_details() to display the car details.

Task:
 Create at least three Car objects.
 Call the display_details() method for each object and display the information.
"""
class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_details(self):
        print(f"\nBrand name: {brand}\nModel name: {model}\nPrice: {price}")



brand = input("Enter the brand name: ")
model = input("Enter the model name: ")
price = float(input("Enter the price: "))

c1 = Car(brand,model,price)

brand = input("Enter the brand name: ")
model = input("Enter the model name: ")
price = float(input("Enter the price: "))

c2 = Car(brand,model,price)

brand = input("Enter the brand name: ")
model = input("Enter the model name: ")
price = float(input("Enter the price: "))

c3 = Car(brand,model,price)

c1.display_details()
c2.display_details()
c3.display_details()