"""
(Composition) [PDF Q71] Create House and Room classes where the rooms are created inside House.
Show composition and explain the lifecycle difference.
"""

class Room:
    def __init__(self):
        self.room = "Room"
        pass

class House:
    def __init__(self):
        self.r1 = Room()
        self.r2 = Room()
        self.r3 = Room()
    def display(self):
        print(f"Rooms is: {self.r1.room} {self.r2.room} {self.r3.room}")

h = House()
h.display()

#deleting
del h

try:
    h.display()
except Exception as e:
    print(e)