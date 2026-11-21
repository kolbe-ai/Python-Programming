"""
Create a Library class that contains multiple Book objects.
Implement methods to add, remove, and display books.
Show that if the Library is deleted, the books also get deleted.
"""

class Library:
  def __init__(self):
    self.books = []
  def add(self,id,author,title):
    new_book = Book(id,author,title)
    self.books.append(new_book)
  def remove(self,book_id):
    for i in self.books:
      if i.id == book_id:
        self.books.remove(i)
  def display(self):
    for i in self.books:
      print(f"Book ID: {i.id}\tAuthor: {i.author}\tTitle:{i.title}\n")


class Book:
  def __init__(self,id,author,title):
    self.id = id
    self.author = author
    self.title = title
  def display(self):
    print(f"Book ID: {self.id}\nAuthor: {self.author}\nTitle: {self.title}\n\n")


lib = Library()
lib.display()

lib.add("101","JK Rowling","Harry Poter")
lib.add("102","Henry","Lion king")
lib.add("103","Job","Jungle book")
lib.add("104","Robin","Spiderman")

lib.display()
lib.remove("105")       #removes book with id 105

print("Deleting the library instance...")
del(lib)
#lib.display()       #shows error