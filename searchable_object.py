from enemy import *
from item import *
from combat import *
from player import *
import random
import time

class Searchable_object():
    def __init__(self, name, item_chance, items, enemies):
        self.name = name
        self.item_chance = item_chance
        self.items = items
        self.enemies = enemies
    
    def search(self):
        randnum = random.randint(1, 100)
        time.sleep(1)
        if randnum <= self.item_chance:
            itemnum = random.randint(0, len(self.items)-1)
            item = self.items[itemnum]
            laika.items.append(item)
            print(f"After searching resolutely Laika found a {item.name}")
            return True
        else:
            enemynum = random.randint(0, len(self.enemies)-1)
            enemy = self.enemies[enemynum]
            print(f"Laika failed to find a useful item, but she did find {enemy.name}")
            return battle(laika, enemy)

comet = Searchable_object("the comet", 100, [low_quality_kibble, jet_fuel, rebar], [])
meteor = Searchable_object("the meteor", 100, [low_quality_kibble, jet_fuel, rebar], [])
derelict_sattelite = Searchable_object("the derelict sattelite", 80, [standard_issue_kibble, sandpaper, jagged_fins, adrenaline], [space_bandit, space_rock])
abandoned_space_station = Searchable_object("the abanoned space station", 70, [standard_issue_kibble, sandpaper, jagged_fins, adrenaline], [space_bandit, space_rock])
cheese_shop = Searchable_object("a shop that sells moon cheese, you're not above stealing", 100, [hyperactive_cheese, wenslydale], [shopkeeper])
cheese_shop2 = Searchable_object("another shop that sells moon cheese, you're still not above stealing", 0, [hyperactive_cheese, wenslydale], [shopkeeper])
abandoned_craft = Searchable_object("an abandoned craft", 66, [window_sealant, luxury_quality_kibble, wd40, new_batteries], [space_bandit])
abandoned_craft2 = Searchable_object("a second abandoned craft", 66, [booster_rocket, adrenaline, nitros, jagged_fins], [space_bandit])
jovian_surface = Searchable_object("the surface of Jupiter", 50, [corrosive_acid, reinforced_steel, nose_armour], [strange_ship, cheese_monster])
uranian_surface = Searchable_object("the surface of Uranus", 50, [[nose_armour, chainmail, wenslydale]], [strange_ship, cheese_monster])