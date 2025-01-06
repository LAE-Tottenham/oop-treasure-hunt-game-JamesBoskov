from InquirerPy import inquirer
from enemy import *
from searchable_object import *
from misc_functions import *

class Place():
    def __init__(self, given_name, next_places, start_text, other_text, enemies, searchable_objects, victory_text, send_to_debris=False, locked=True):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.next_places = next_places
        self.searchable_objects = searchable_objects
        self.start_text = start_text
        self.other_text = other_text
        self.enemies = enemies
        self.send_to_debris = send_to_debris
        self.locked = locked
        self.victory_text = victory_text
        self.proggress = 0

    def set_next_places(self, place_instances):
        self.next_places = place_instances

    def start(self):
        if self.send_to_debris:
            self.send_to_debris = False
            return True
        
        if self.name == "home":
            print("well done brave traveller, you have won")
            print("game complete.")
        else:
            return self.do_something(self.start_text)
    
    def do_something(self, text): # I realise this is a bad name but this function just gets the user to do something
        choice = self.get_command(text)
        if isinstance(choice, Place):
            return choice
        if isinstance(choice, Enemy):
            print(choice.description)
            str(input("\npress enter to continue"))
            result = battle(laika, choice)
            if result:
                print(self.victory_text)
                if choice.unlocks != None:
                    print(get_unlocks_output(choice))
                    for i in choice.unlocks:
                        for j in places:
                            if j.name == i:
                                j.locked = False
                self.enemies.remove(choice)
                self.proggress += 1
                if self.proggress == 9:
                    Home.locked = False
                print("The last part of your ship has been gathered, you feel ready to depart from this cosmic adventure.")
                return self.do_something(self.other_text)
            return "checkpoint"
        result = choice.search()
        if result:
            self.searchable_objects.remove(choice)
            return self.do_something(self.other_text)
        return "checkpoint"

    def get_command(self, text):
        choices = {}
        for i in self.next_places:
            if not i.locked:
                choices[f"travel to {i.name}"] = i
        for i in self.enemies:
            choices[f"fight {i.name}"] = i
        for i in self.searchable_objects:
            choices[f"search {i.name}"] = i
        command = inquirer.select(
            message=text,
            choices=list(choices.keys()),
        ).execute()
        return choices[command]

# defines all the places for the story
Home = Place("home", None, None, None, None, None, None)
Orbit = Place("orbit", [], "Welcome to orbit, you are currently circling around the earth at a speed of seven and a half kilometres a second. You may be alone in the vast expanse of space, but you do have some ideas as to what you want to do. You could: ", "what else would you like to do in orbit",
               [space_rock], [test_closet], "Well done on pulverising that murderous peice of nickel, in the ensueing cloud of smoke you managed to find your rocket's fins, in the words of Borat, 'great success'", 
               False, False)
Geostationary_Orbit = Place("geostationary orbit", [], "welcome to geostationary orbit, write some more stuff", "what else would you like to do in geostationary orbit", [], [], False, False)
Moon = Place("the Moon", [], "welcome to the Moon, write some more stuff", "what else would you like to do on the moon", [], [], "", False, False)
Mars = Place("Mars", [], "welcome to Mars, write some more stuff", "what else would you like to do on Mars", [], [], "", False, False)
Interstellar_Highway = Place("the interstellar highway", [], "welcome to the interstellar highway, write some more stuff", None, [], [], "", True)
Debris_Field = Place("the debris field", [], "welcome to the debris field, write some more stuff", "what else would you like to do in the debris field", [], [], "")
Jupiter = Place("Jupiter", [], "welcome to Jupiter, write some more stuff", "what else would you like to do on Jupiter",[], [], "")
Uranus = Place("Uranus", [], "welcome to Uranus, write some more stuff", "what else would you like to do on Uranus", [], [], "")
Strange_Space_Craft = Place("the strange space craft", [], "welcome to the strange space craft, write some more stuff", "what else would you like to do on the strange space craft", [], [], "")
Abyss = Place("the abyss", [], "welcome to the abyss, write some more stuff", "what else would you like to do in orbit", [], [], "")

# defines how the player can move between places in the story
Orbit.set_next_places([Moon, Geostationary_Orbit, Mars, Home, Interstellar_Highway])
Geostationary_Orbit.set_next_places([Orbit, Mars])
Moon.set_next_places([Mars, Orbit])
Mars.set_next_places([Interstellar_Highway, Geostationary_Orbit, Moon])
Interstellar_Highway.set_next_places([Orbit, Geostationary_Orbit, Moon, Mars, Debris_Field, Jupiter, Uranus, Strange_Space_Craft, Abyss])
Jupiter.set_next_places([Interstellar_Highway])
Uranus.set_next_places([Interstellar_Highway])
Strange_Space_Craft.set_next_places([Interstellar_Highway])
Abyss.set_next_places([Interstellar_Highway])
places = [Orbit, Geostationary_Orbit, Moon, Mars, Interstellar_Highway, Jupiter, Uranus, Strange_Space_Craft, Abyss]