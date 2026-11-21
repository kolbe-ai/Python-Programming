"""
Using the concept of arbitrary keyword arguments, write a function to collect details from a customer and display them as (key: value) pairs.
"""

def details(**kwargs):
  for key,values in kwargs.items():
    print(f"{key} : {values}")

id = input("Enter PID: ")
name = input("Enter Product name: ")
price = float(input("Enter the price: "))
quty = int(input("Enter the quantity: "))

details(p_id = id,p_name = name, p_price = price, quantity = quty)

