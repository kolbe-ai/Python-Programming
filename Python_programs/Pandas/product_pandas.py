"""
20. Given product data containing Product ID, Product Name, Category,
Price and Quantity, create a DataFrame. Add a Total column using
Price × Quantity, find the total sales by category, and display products
whose total value exceeds a specified amount.
"""

import pandas as pd
data = {"P_id": [1,2,3],"Name": ["Shoes","Mangos","Ice"],"Category": ["Items","Fruits","Ice"],"Price": [10,20,30]}
df = pd.DataFrame(data)
quant = [30,20,10]
df["Quantity"] = quant
print(df)

#printing after adding
df["Total"] = df["Price"] * df["Quantity"]
print("\n\nDetails:")
print(df)

#find the total sales by category, and display products whose total value exceeds a specified amount.
print("\n\nTotal sales by category:")
total = df.groupby("Category")["Total"].sum()
print(total)