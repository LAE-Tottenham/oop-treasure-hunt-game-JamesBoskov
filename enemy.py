from moves import *
from item import *

class Enemy():
    def __init__(self, name,  moves, health, attack, defense, speed, description, item, unlocks):
        self.name = name
        self.stats = {"health" : health,
                      "attack" : attack,
                      "defense" : defense,
                      "speed" : speed}
        self.current_stats = dict(self.stats)
        self.moveset = moves
        self.description = description
        self.item = item
        self.unlocks = unlocks

test_goon = Enemy("test goon", [booster_bounce], 12, 10, 15, 10, "vague test goon", blowtorch, ["the interstellar highway"])
space_rock = Enemy("an evil space rock", [stand_there], 12, 10, 15, 10, "This is just a rock, it is not sentient nor can it really attack you, but it has part of your space craft and your not gonna let something as stupid as it being inanimate stop you from crushing it with the full power of mighty Russia, Stalin would be very proud",
                    None, None)