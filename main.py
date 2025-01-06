from place import *
from player import *
from item import *
from pyfiglet import Figlet

class Game():
    def __init__(self):
        self.current_place = None
        self.checkpoint = Orbit
    
    def set_current_place(self, new_place):
        self.current_place = new_place
        return self.current_place.start()

f = Figlet(font='slant')
print(f.renderText("Welcome to Laika's Big Adventure"))

print("You are Laika, on of the first animals ever sent into space by the great USSR. You have just been launched into space but unfortunately your rocket has collided with a comet just after passing the Karman line, if you want any chance of getting back home you'll have to find the missing parts of your space ship that have been scattered throughout the galaxy. Good luck.")

Game_Instance = Game()
next_place = Game_Instance.set_current_place(Orbit)
while True:
    if next_place != "checkpoint":
        next_place = Game_Instance.set_current_place(next_place)
    else:
        next_place = Game_Instance.set_current_place(Game_Instance.checkpoint)