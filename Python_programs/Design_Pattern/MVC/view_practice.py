"""
(Design Pattern: MVC) [PDF Q75]
A tiny Book Manager with Model (title, author), View (display), and Controller (add/list).
Explain what each part does.
"""

class View:
    def display(self,obj):
            print(f"\n\nTitle: {obj.title}\nAuthor: {obj.author}")
