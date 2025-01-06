from moves import *
from item import *

class Enemy():
    def __init__(self, name,  moves, health, attack, defense, speed, title, item, unlocks):
        self.name = name
        self.stats = {"health" : health,
                      "attack" : attack,
                      "defense" : defense,
                      "speed" : speed}
        self.current_stats = dict(self.stats)
        self.moveset = moves
        self.title = title
        self.item = item
        self.unlocks = unlocks

test_goon = Enemy("test goon", [booster_bounce], 12, 10, 15, 10, "vague test goon", blowtorch, ["the interstellar highway"])