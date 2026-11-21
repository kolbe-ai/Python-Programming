"""
31. Create a Distance class representing distance in kilometres and
metres. Overload the + operator to add two Distance objects and
display the resulting distance in normalized form.
"""

class Distance:
    def __init__(self,km,m):
        self.km = km
        self.m = m
    def __add__(self,other):
        return Distance(self.km+other.km , self.m+other.m)
    def display(self):
        print(f"{self.km}km {self.m}m ")

d1 = Distance(10,20)
d2 = Distance(19,2)
d3 = d1+d2
d3.display()