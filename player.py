import random
from moves import * 

class Player():
    def __init__(self, moves):
        self.stats = {"health" : 18 + random.randint(1, 5),
                      "attack" : 18 + random.randint(1, 5),
                      "defense" : 18 + random.randint(1, 5),
                      "speed" : 18 + random.randint(1, 5)}
        self.current_stats = dict(self.stats)
        self.moveset = {"booster bounce" : moves["booster bounce"], 
                        "menacing bark" : moves["menacing bark"]}

    def calculate_inventory_size(self):
        pass

    def add_item(self, item_instance):
        pass

    def use_item(self, item_instance):
        pass

    def add_move(self, moves, move):
        pass
    # add more methods as needed

laika = Player(moves)