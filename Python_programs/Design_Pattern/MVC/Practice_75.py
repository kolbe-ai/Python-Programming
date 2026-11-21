"""
75. (MVC) Build a Student Management System using MVC.
The Model holds student data (name, roll number, marks),
the View displays the details, and
the Controller handles input and updates the model and view.
"""

class Model:
    def __init__(self):
        self.name = None
        self.rno = None
        self.mark = None
class View:
    def display(self,model):
        print(f"\n\nStudent Details: \nStudent name: {model.name}\nRoll no: {model.rno}\nMark: {model.mark}\n")
class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
    def user_input(self):
        self.model.name = input("Enter the name: ")
        self.model.rno = int(input("Enter the rno: "))
        self.model.mark = float(input("Enter the mark: "))
        self.view.display(self.model)
    def update_input(self):
        self.model.mark = float(input("Enter the updated mark: "))
        self.view.display(self.model)

m = Model()
v = View()
c = Controller(m,v)

c.user_input()
c.update_input()
