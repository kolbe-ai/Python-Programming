"""
3. Create a simple Library Management application using MVC
architecture. The Model should maintain book title, author and
availability status. The View should display book details, while the
Controller should handle adding and searching for books.
"""
from zoneinfo import available_timezones

from library_3_model import Model
from library_3_view import View
class Controller:
    def __init__(self):
        self.Model = Model()
        self.View = View()
    def controller(self):
        #inserting values
        while(True):
            print("Enter 1 to insert\nEnter 0 to exit: ")
            choice = int(input("Enter the choice: "))
            if (choice == 1):
                id = int(input("Enter the book id: "))
                title = input("Enter the book title: ")
                author = input("Enter the author: ")
                available = input("Enter (yes) or (no): ")
                self.Model.add_book(id,title,author,available)
            else:
                break

        ##showing details
        library = self.Model.get_book()
        self.View.view_all(library)

if __name__ == "__main__":
    x = Controller()
    x.controller()