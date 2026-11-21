#Create Vector with x, y. Overload +, -, and ==

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x , self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x , self.y - other.y)
    def __eq__(self,other):
        return self.x == other.x and other.x == other.y
    def display(self):
        print(f"{self.x}x + {self.y}y")

v1 = Vector(1,2)
v2 = Vector(2,3)
v3 = v1+v2
v4 = v2-v1
print("Added:")
v3.display()
print(f"Sub: ")
v4.display()
print("Equal: ",v1==v2)