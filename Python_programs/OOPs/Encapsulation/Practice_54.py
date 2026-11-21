"""
54. Define a Student class with a protected name and a private mark.
Provide setters for both, accepting marks only between 0 and 100, plus a protected method to display name and marks.
Demonstrate the class following Python’s access conventions: protected members accessed appropriately, private members hidden from outside.
"""


class Student:
    def __init__(self,name = None,mark=None):
        self._name = name
        self.__mark = mark
    def set_details(self,name,mark):
        self._name = name
        if (mark <= 100 and mark>=0):
            self.__mark = mark
        else:
            print("Invalid mark!")
            return
    def _display(self):
        print(f"\nName: {self._name}\nMark: {self.__mark}")

s1 = Student()
s1.set_details("Ravi",100)
s1._name = "Ragav"
s1._display()


"""
From GEMINI

class Student:
    def __init__(self, name=None, mark=None):
        self._name = name       # Protected attribute
        self.__mark = mark      # Private attribute

    # Separate setter for name
    def set_name(self, name):
        self._name = name

    # Separate setter for mark with validation
    def set_mark(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark
        else:
            print("Invalid mark! Must be between 0 and 100.")

    # Protected method
    def _display(self):
        print(f"Name: {self._name}\nMark: {self.__mark}")


# Subclass demonstrating appropriate access to protected members
class ReportCard(Student):
    def show_report(self):
        print("\n--- Student Report ---")
        # Accessing protected attribute and protected method inside a subclass
        self._display()


# --- Demonstration ---
s1 = ReportCard()
s1.set_name("Ravi")
s1.set_mark(95)
s1.show_report()

# Testing invalid mark
s1.set_mark(150)  # Prints error and keeps 95 safe

# Demonstrating that private attribute '__mark' is hidden from outside
try:
    print(s1.__mark)
except AttributeError:
    print("\nAccess Denied: '__mark' is private and hidden from outside!")
"""