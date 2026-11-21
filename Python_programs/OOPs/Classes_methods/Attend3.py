"""
Question 3: Book Management
Create a Book class with the following:
 Attributes: book_id, title, author, price
 Method:
o display_book() to display all book details.

Task:
 Create at least three Book objects.
 Call the display_book() method for each object to display the details.
"""

class Book:
    def __init__(self,book_id,title,author,price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
    def display_book(self):
        print(f"\nBook ID: {book_id}\nTitle: {title}\nAuthor: {author}\nPrice: {price}")

book_id = int(input("Enter the book id: "))
title = input("Enter the book title: ")
author = input("Enter the book author: ")
price = float(input("Enter the book price: "))
b1 = Book(book_id, title, author, price)

book_id = int(input("Enter the book id: "))
title = input("Enter the book title: ")
author = input("Enter the book author: ")
price = float(input("Enter the book price: "))
b2 = Book(book_id,title, author, price)

book_id = int(input("Enter the book id: "))
title = input("Enter the book title: ")
author = input("Enter the book author: ")
price = float(input("Enter the book price: "))
b3 = Book(book_id,title, author, price)

b1.display_book()
b2.display_book()
b3.display_book()