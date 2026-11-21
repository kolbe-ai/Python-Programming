"""
32. Create a Book class with title and price. Overload the < operator to
compare two books based on their prices. Also overload == to check
whether two books have the same price.
"""

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    def __gt__(self,other):
        return (self.price> other.price)
    def __eq__(self,other):
        return (self.price == other.price)

b1 = Book("Harry potter",12345)
b2 = Book("Disney",234543)
print(b1>b2)
b3 = Book("Nothing",12345)
print(b1==b3)
print(b1 == b2)