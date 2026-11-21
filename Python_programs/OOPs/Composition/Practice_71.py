"""
71. (Composition)
Create a Library class containing multiple Book objects, with methods to add, remove and display books.
Show that deleting the Library also deletes its books.
"""

class Book:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name: ",self.name)

class Library:
    def __init__(self):
        self.books = []
    def add(self,name):
        self.book= Book(name)
        self.books.append(self.book)
    def remove(self,book):
        for i in self.books:
            if i.name == book:
                self.books.remove(i)
    def display(self):
        print("\n\nBooks are: ")
        for i in self.books:
            i.display()

l = Library()
l.add("Jungle Book")
l.add("Big Hero 6")
l.add("Hello Kitty")
l.add("Nothing book")
l.display()
l.remove("Nothing book")
l.display()

del l
try:
    print("\n\nAfter deleting: ")
    l.display()
except Exception as e:
    print(e)