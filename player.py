import random
from moves import * 

class Player():
    def __init__(self, booster_bounce, menacing_bark):
        self.stats = {"health" : 18 + random.randint(1, 5),
                      "attack" : 18 + random.randint(1, 5),
                      "defense" : 18 + random.randint(1, 5),
                      "speed" : 18 + random.randint(1, 5)}
        self.current_stats = dict(self.stats)
        self.moveset = [booster_bounce, menacing_bark]
        self.items = []

    def calculate_inventory_size(self):
        pass

    def add_item(self, item_instance):
        self.items.append(item_instance)

    def use_item(self, item_instance):
        self.items.remove(item_instance)

    def add_move(self, move):
        self.moveset[move["name"]] = move

    # add more methods as needed

laika = Player(booster_bounce, menacing_bark)
