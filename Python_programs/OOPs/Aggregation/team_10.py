"""
10. Create a Team class and a Player class using aggregation. A team
should contain multiple play
"""

class Team:
    def __init__(self,t_name):
        self.team = t_name
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def display(self):
        print("\n",self.team,":\n")
        for i in self.players:
            print(f"Player Name: {i.p_name}")

class Player:
    def __init__(self,p_name):
        self.p_name = p_name
    def display(self):
        print(f"Player Name: {self.p_name}")

t = Team("Liverpool")
p1 = Player("Salah")
t.add_player(p1)
p2 = Player("Fernando")
t.add_player(p2)
p3 = Player("Arnold")
t.add_player(p3)
t.display()

#after deleting
del t
print(f"\n\nAfter Deleting Liverpool: \n")
p1.display()
p2.display()
p3.display()