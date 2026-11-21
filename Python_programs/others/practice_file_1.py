import numpy as np
"""
arr = np.array([[1,2],[3,4]])
print(arr)
arr = np.arange(0,20).reshape(4,5)
print(arr)
"""

"""
num = input("Enter a number: ")
count = len(num)
num = int(num)
temp = num
arm = 0
while(temp!= 0):
    digit = temp%10
    arm += digit**count
    temp = temp//10

if (num == arm):
    print("Armstrome")
else:
    print("Not armstrome")
"""

"""
class MyRange:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        for i in range(self.num):
            yield i
        return self
iter1 = MyRange(10)
it = iter(iter1)
print(next(it))
print(next(it))
"""

"""
# Create a class BankAccount with private attributes __balance. Provide methods to deposit,
#withdraw, and check balance while preventing direct modification.

class BankAccount:
    __balance = None
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print("Balance is: ",self.__balance)
    def withdraw(self,amount):
        self.__balance -= amount
        print("Balance is: ",self.__balance)

b = BankAccount(1000)
b.deposit(123)
b.withdraw(10)
"""

"""
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before decor")
        func(*args,**kwargs)
        print("After decor")
    return wrapper

@decorator
def greet():
    print("Hello")
greet()
"""

"""
class FileManager:
    def __init__(self,file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file = None
    def __enter__(self):
        self.file = open(self.file_name,self.file_mode)
        return self.file
    def __exit__(self,*args):
        self.file.close()
        return
with FileManager("example.txt","w") as f:
    f.write("Hello")
with FileManager("example.txt","r") as f:
    x = f.read()
    print(x)
"""


"""
#abstraction
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def type(self):
        print("Animal")
class Dog(Animal):
    def make_sound(self):
        print("Buff Buff")
d = Dog()
d.type()
"""

"""
#types of method
class School:
    name = "ABC School"
    no = 1234
    def __init__(self,s_id):
        self.s_id = s_id
    def std(self):
        print("SID is: ",self.s_id)
    @classmethod
    def School_name(cls):
        print("School name is: ",cls.name)
    @staticmethod
    def check_student(id):
        if(id<0):
            print("Invalid ID")
        else:
            print("Valid ID")

s = School(123)
s.std()
School.School_name()
School.check_student(123)
"""

"""
#Logger
class Log:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
Log1 = Log()
Log2 = Log()
print(Log1 is Log2)
"""

"""
#Composition
class House:
    def __init__(self,num):
        self.num = num
class Room:
    def __init__(self,size):
        self.size = size
        self.house = House(10)
    def display(self):
        print(f"Size: {self.size}\nHouse: {self.house.num}")
r1 = Room(100)
r1.display()
del r1
"""
"""
#Aggregation
class Job:
    def __init__(self,job):
        self.job = job
class Employee:
    def __init__(self,name,job):
        self.name = name
        self.job = job
    def display(self):
        print(f"Name: {self.name}\nJob: {self.job.job}")
j1 = Job("Software Devoloper")
e1 = Employee("Ravi",j1)
del j1
e1.display()
"""

"""
#singleton instance
class Log:
    _instance = None
    def __new__(cls):
        if (cls._instance == None):
            cls._instance = super().__new__(cls)
        return cls._instance

l1 = Log()
l2 = Log()
print(l1 == l2)
"""

"""
#MVC model
class Model:
    def __init__(self,sid,sname):
        self.sid = sid
        self.name = sname
    def update(self,sid,name):
        self.sid = sid
        self.name = name
class View:
    def __init__(self,model):
        self.model = model
    def display(self):
        print(f"\nStudent ID: {self.model.sid}\nStudent Name: {self.model.name}\n")
class Controller:
    def __init__(self):
        m = Model(101,"Ravi")
        v = View(m)
        v.display()
if __name__ == "__main__":
    c = Controller()
"""

"""
class Point:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def __add__(self,other):
        return Point(self.num1 + other.num1, self.num2+other.num2)
p1 = Point(1,2)
p2 = Point(2,3)
p3 = p1+p2
print(p3.num1,p3.num2)
"""
