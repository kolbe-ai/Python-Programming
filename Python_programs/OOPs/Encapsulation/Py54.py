"""
Define a class Student with a protected attribute name and a private attribute mark.
Provide setter methods to update both values, ensuring that marks can only be set if they are between 0 and 100.
Include a protected method to display the student’s name and marks.
Finally, demonstrate the functionalities of the class by accessing its methods and attributes according to Python’s access modifier conventions,
where protected members are accessed appropriately and private members remain hidden from outside the class.
"""

class Student:
    def __init__(self,name,mark):
        self._name = name
        self.__mark = mark
    def set_name(self,name):
        self._name = name
    def set_mark(self,mark):
        if (mark<=100 and mark>=0):
            self.__mark = mark
        else:
            print(f"Invalid mark")
    def _display(self):
        print(f"\nName: {self._name}\nMark: {self.__mark}")

#displaying the student
s1 = Student("Golan",98)
s1.set_mark(100)
s1._display()

#changing the protected data (it changes)
s1._name = "Nalog"
s1._display()

#trying to change protected data (doesn't change)
s1.__mark = 97
s1._display()