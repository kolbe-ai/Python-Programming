"""
Question 1 — Easy
Create a Product Management System using the MVC pattern.

Model: Store product name, product ID, and price.

View: Display product details.

Controller: Add products and display product details.
"""

class Model:

    def __init__(self):
        self.product = {1: {"Name" : "Hello", "Price": 0}}
    def add_item(self,id,name,price):
        self.product[id] = {"Name": name,"Price": price}
    def get_item(self):
        return self.product