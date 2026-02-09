from random import randint

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = randint(0, 100) * 0