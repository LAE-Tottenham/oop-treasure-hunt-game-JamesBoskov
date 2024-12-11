import random
class Player():
    def __init__(self, moves):
        self.health = 18 + random.randint(1, 5)
        self.attack = 18 + random.randint(1, 5)
        self.defense = 18 + random.randint(1, 5)
        self.speed = 18 + random.randint(1, 5)
        self.moveset = [moves["booster bounce"], moves["menacing growl"]]

    def calculate_inventory_size(self):
        pass

    def add_item(self, item_instance):
        pass

    def use_item(self, item_instance):
        pass

    def add_move(self, moves, move):
        pass
    # add more methods as needed

moves = [{"booster bounce": {"name" : "booster bounce", "power" : 5, "effect" : None}}, 
{"menacing growl" : {"name" : "menacing growl", "effect" : "atk"}}]