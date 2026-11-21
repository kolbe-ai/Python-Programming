"""
(Aggregation) [PDF Q70] Create Department and Teacher classes. Show that a Teacher survives when the Department is deleted.
"""


class Department:
    def __init__(self, dept,teacher):
        self.dept = dept
        self.teacher = teacher
    def display(self):
        self.teacher.display()
        print(f"Department: {self.dept}\n")


class Teacher:
    def __init__(self, name, id, sal):
        self.name = name
        self.id = id
        self.sal = sal

    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nSalary: {self.sal}\n\n")


t = Teacher("Rahul", 101, 200000)
d = Department("Computer",t)
t.display()
d.display()

# deleting department
del d
t.display()
