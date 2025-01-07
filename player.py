import random
from moves import * 
from InquirerPy import inquirer

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
        self.progress = 0

    def calculate_inventory_size(self):
        if len(self.items) > 10:
            item_dict = {}
            for i in self.items:
                item_dict[i.name] = i
            choices = list(item_dict.keys)
            removed_item = inquirer.select(
                message="Oh no! Your inventory is to heavy, you must choose to remove an item",
                choices=choices,
            ).execute()
            self.items.remove(item_dict[removed_item])

laika = Player(booster_bounce, menacing_bark)
