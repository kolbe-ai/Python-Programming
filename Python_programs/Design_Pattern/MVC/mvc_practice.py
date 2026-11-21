"""
Question 1 — Easy
Create a Product Management System using the MVC pattern.
Model: Store product name, product ID, and price.
View: Display product details.
Controller: Add products and display product details.
"""

from mvc_view import View
from mvc_model import Model

class Controller:
    def __init__(self):
        self.Model = Model()
        self.View = View()

    def controller(self):
        self.Model.add_item(1,"Book",100)
        self.Model.add_item(2,"Food",200)
        info = self.Model.get_item()
        self.View.display(info)

if __name__ == "__main__":
    x = Controller()
    x.controller()