from random import randint

class Player:
    def __init__(self, name: str):
        self.name = name
        self.id = randint(0, 10**100)