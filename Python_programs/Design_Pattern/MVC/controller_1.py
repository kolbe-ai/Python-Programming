"""
Implement a Student Management System using the MVC pattern:
● Model: Student data (name, roll number, marks).
● View: Display student details.
● Controller: Handle input and update model/view.
"""

from model_1 import s_model
from view_1 import v_view


class controller:
    def __init__(self):
        self.s_model = s_model()
        self.v_view = v_view()
    def controller1(self):
        #st1 = {103,"Rohit"}
        self.s_model.add_item(103,"Rohit")
        st1 = self.s_model.current_item()
        self.v_view.view_all(st1)

if __name__ == "__main__":
    f = controller()
    f.controller1()