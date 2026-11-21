"""
Maintain a shopping cart list with add, remove, “is item present?”, and sorted display (like the passenger tracker).
"""

shopping_cart = ["shoes","fruits","tools","butter"]
shopping_cart.append("Laptop")
print(shopping_cart)
shopping_cart.remove("tools")
print(shopping_cart)

item = input("Enter the search item: ")
if item in shopping_cart:
  print("Item contains in shopping card")

print("Sorted: ",sorted(shopping_cart))