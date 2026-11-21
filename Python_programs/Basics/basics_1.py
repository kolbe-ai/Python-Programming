"""
Take a product price and quantity, then print the total with 18% GST added. Show the output using all four formatting styles (concatenation, format(), f-string, %).
"""

price = float(input("Enter the price: "))
quantity = int(input("Enter the price: "))

total = price*quantity
total = total + (total*18/100)
print("The total with GST is: ",total)
print(f"The total with GST is: {total}")
print("The total with GST is: {}".format(total))
print("The total with GST is: %.2f" %(total))