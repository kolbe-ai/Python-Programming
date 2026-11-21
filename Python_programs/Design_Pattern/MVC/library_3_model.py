"""
3. Create a simple Library Management application using MVC
architecture. The Model should maintain book title, author and
availability status. The View should display book details, while the
Controller should handle adding and searching for books.
"""

class Model:
    def __init__(self):
        self.library = {1: {"title": "" ,"author": "" ,"availability": ""}}
    def add_book(self,bookid,title,author,avail):
        self.library [bookid] = {"title": title,"author": author,"availability": avail }
    def get_book(self):
        return self.library