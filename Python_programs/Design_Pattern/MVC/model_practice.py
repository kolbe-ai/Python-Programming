"""
(Design Pattern: MVC) [PDF Q75]
A tiny Book Manager with Model (title, author), View (display), and Controller (add/list).
Explain what each part does.
"""

class Model:
    def __init__(self,title,author):
        self.title = title
        self.author = author