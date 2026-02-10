from player import Player

class Table:
    def __init__(self, id: int, p1: Player, p2: Player, p3: Player, p4: Player, initalScore: int):
        self.id = id
        
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

        self.s1 = initalScore
        self.s2 = initalScore
        self.s3 = initalScore
        self.s4 = initalScore