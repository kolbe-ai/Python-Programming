"""
(Encapsulation: Protected vs Private) [PDF Q54] Create Employee with a protected _salary and private __id. Show access from a subclass and from outside.
"""


class Employee:
    def __init__(self, salary, id):
        self._salary = salary
        self.__id = id

    def display(self):
        print(f"\nID: {self.__id}\nSalary: {self._salary}")


class Manager(Employee):
    def check(self):
        print("Manager can access: ", self._salary)
        # print("Manager can access: ",self.__id) cannot access


e = Employee(10000, 101)
e.display()
m = Manager(200000, 100)
m.check()

print("Trying to access: ")
print(m._salary)
print(e._salary)

"""Error will occur because it protected
print(m.__id)
print(e.__id)
"""

