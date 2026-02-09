from player import Player

class Game:
    def __init__(self, p1: Player, p2: Player, p3: Player, p4: Player):
        self.players = [
            p1,
            p2,
            p3,
            p4
        ]