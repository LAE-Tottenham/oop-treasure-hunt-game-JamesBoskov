from moves import *
import random

class Enemy():
    def __init__(self, moves, health, attack, defense, speed):
        self.stats = {"health" : health,
                      "attack" : attack,
                      "defense" : defense,
                      "speed" : speed}
        self.current_stats = dict(self.stats)
        self.moveset = moves

test_goon = Enemy({"booster bounce" : moves["booster bounce"]}, 12, 10, 15, 10)