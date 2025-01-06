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
print(Game_Instance.set_current_place(Orbit).name)