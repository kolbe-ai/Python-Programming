"""
(Design Pattern: MVC) [PDF Q75]
A tiny Book Manager with Model (title, author), View (display), and Controller (add).
Explain what each part does.
"""

from model_practice import Model
from view_practice import View

class Controller:
    books = []
    def __init__(self):
        self.books = []
        self.view = View()
    def add(self,title,author):
        model = Model(title,author)
        self.books.append(model)                 #adding books
        self.view.display(model)
if __name__ == "__main__" :
    c = Controller()
    c.add("Harry Poter","JK rowling")
    c.add("Jungle book","Disney")



