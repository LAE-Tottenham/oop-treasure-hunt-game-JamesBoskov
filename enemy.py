from moves import *

class Enemy():
    def __init__(self, name,  moves, health, attack, defense, speed, title):
        self.name = name
        self.stats = {"health" : health,
                      "attack" : attack,
                      "defense" : defense,
                      "speed" : speed}
        self.current_stats = dict(self.stats)
        self.moveset = moves
        self.title = title

test_goon = Enemy("test goon", [booster_bounce], 12, 10, 15, 10, "vague test goon")