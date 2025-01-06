from place import *
from player import *
from item import *

class Game():
    def __init__(self):
        self.current_place = None
        self.checkpoint = Orbit
    
    def set_current_place(self, new_place):
        self.current_place = new_place
        return self.current_place.start()

        
Game_Instance = Game()
next_place = Game_Instance.set_current_place(Orbit)
while True:
    if next_place != "checkpoint":
        next_place = Game_Instance.set_current_place(next_place)
    else:
        next_place = Game_Instance.set_current_place(Game_Instance.checkpoint)