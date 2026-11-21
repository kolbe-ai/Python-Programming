"""
11. Create a Library class that contains multiple Book objects.
Implement methods to add, remove, and display books. Show that if
the Library is deleted, the books also get deleted.
"""

class Library:
    def __init__(self,name):
        self.name = name
        self.book = []
    def add_book(self,b_name):
        self.book.append(b_name)

    def remove_book(self, b_name):
        for book in self.book:
            if book.b_name == b_name:
                self.book.remove(book)
                break

    def display(self):
        for i in self.book:
            print(f"Book name: {i.b_name}")

class Book:
    def __init__(self, b_name):
        self.b_name = b_name
    def display(self):
        print(f"Book name: {self.b_name}")


#adding data
lib = Library("City Library")
b1 = Book("Harry Potter")
lib.add_book(b1)
b2 = Book("Jungle Book")
lib.add_book(b2)
b3 = Book("Snow White")
lib.add_book(b3)
b4 = Book("Disney")
lib.add_book(b4)
print("\nLibrary :")
lib.display()

#deleting a book
lib.remove_book("Jungle Book")
print("\nLibrary :")
lib.display()

#after deeleting library
del lib
#lib.display()
