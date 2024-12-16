import random
from moves import * 
from place import *

class Player():
    def __init__(self, booster_bounce, menacing_bark):
        self.stats = {"health" : 18 + random.randint(1, 5),
                      "attack" : 18 + random.randint(1, 5),
                      "defense" : 18 + random.randint(1, 5),
                      "speed" : 18 + random.randint(1, 5)}
        self.name = "Laika"
        self.current_stats = dict(self.stats)
        self.moveset = [booster_bounce, menacing_bark]
        self.items = []
        self.place = orbit
        self.checkpoint = orbit

    def calculate_inventory_size(self):
        pass

    # add more methods as needed

laika = Player(booster_bounce, menacing_bark)
