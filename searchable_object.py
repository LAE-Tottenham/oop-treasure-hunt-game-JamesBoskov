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
        else:
            enemynum = random.randint(0, len(self.enemies)-1)
            enemy = self.enemies[enemynum]
            print(f"Laika failed to find a useful item, but she did find {enemy.name}")
            battle(laika, enemy)

test_closet = Searchable_object("test closet", 80, [blowtorch], [test_goon])