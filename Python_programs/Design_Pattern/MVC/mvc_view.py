"""
Question 1 — Easy
Create a Product Management System using the MVC pattern.

Model: Store product name, product ID, and price.

View: Display product details.

Controller: Add products and display product details.
"""

class View:
    def display(self,item):
        for id,details in item.items():
            print(f"ID: {id}\tName: {details['Name']}\tPrice: {details['Price']}")
