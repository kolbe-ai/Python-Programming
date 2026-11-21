"""
Implement a Student Management System using the MVC pattern:
Model: Student data (name, roll number, marks).
View: Display student details.
Controller: Handle input and update model/view.
"""

from Py75_view import View
from Py75_model import Model

class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
    def controller(self):
        model = self.model("Ravi",1,98)
        self.view.display(model.name,model.no,model.marks)
        model.update(100)      #updating mark
        self.view.display(model.name,model.no,model.marks)

if __name__ == "__main__":
    c = Controller(Model,View)
    c.controller()

