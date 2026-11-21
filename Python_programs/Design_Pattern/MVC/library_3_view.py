"""
3. Create a simple Library Management application using MVC
architecture. The Model should maintain book title, author and
availability status. The View should display book details, while the
Controller should handle adding and searching for books.
"""

class View:
    def view_all(self,book):
        print("\nThe Book Details: ")
        for id,details in book.items():
            print(f"Book ID: {id}\tTitle: {details["title"]}\tAuthor: {details["author"]}\tAvailablity: {details["availability"]}")
