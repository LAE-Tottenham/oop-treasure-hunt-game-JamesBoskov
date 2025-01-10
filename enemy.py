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

space_bandit = Enemy("a space bandit", [fake_out, menacing_bark], 15, 13, 15, 10, "", None, None)
test_goon = Enemy("test goon", [booster_bounce], 12, 10, 15, 10, "vague test goon", blowtorch, ["the interstellar highway"])
space_rock = Enemy("an evil space rock", [stand_there], 12, 10, 15, 10,
                    "This is just a rock, it is not sentient nor can it really attack you, but it has part of your space craft and your not gonna let something as stupid as it being inanimate stop you from crushing it with the full power of mighty Russia, Stalin would be very proud",
                    None, None)
ominous_sattelite = Enemy("a very spoooooooky sattelite", [laser_beam], 15, 14, 12, 20, "This sattelite seems strange, time to kill it", blowtorch, None )
cheese_monster = Enemy("the cheese monster", [cheese_strike], 32, 18, 15, 10, "a fearful amalgamation of molten Wendslydale spews towards you, good luck trying to cheese this fight", hyperactive_cheese, None)
rex = Enemy("Rex, the American dog", [mega_booster_bounce], 32, 20, 20, 20, "Rex the American capitalist pig dog is landing right in front of you, you know what you must do.", None,  ["the interstellar highway"])
strange_ship = Enemy("a small strange ship", [stand_there], 50, 0, 40, 0, "It seems to be scanning you", None, ["the interstellar highway", "Jupiter", "Uranus"])
jovian = Enemy("the jovian", [fake_out, steely_resolve, booster_bounce, all_out_crash], 37, 28, 20, 25, "A tall bipedal creature with red skin and defined musculature steps out from the clouds.", None, ["the strange space craft"])
uranian = Enemy("the uranian", [fake_out, steely_resolve, booster_bounce, all_out_crash], 42, 20, 28, 25, "A tall bipedal creature with blue skin and defined musculature steps out from the clouds.", None, ["the strange space craft"])
alien_warrior = Enemy("the warrior", [spacewalk_scratch, menacing_bark], 40, 40, 20, 20, "A great hulking mass of muscle and skin, it rears up on its hind legs before charging at you.", None, ["the abyss"])
zorgul = Enemy("Zorgul the enemy king", [all_out_crash, steely_resolve], 32, 36, 34, 31, "The leader of this great race of aliens. He looks nervous.", None, None)
shopkeeper = Enemy("an angry shopkeeper", [mega_booster_bounce], 15, 50, 20, 20, "shows you for stealing", None, None)