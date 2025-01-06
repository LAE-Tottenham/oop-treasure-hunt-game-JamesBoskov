from InquirerPy import inquirer
from enemy import *
from searchable_object import *

class Place():
    def __init__(self, given_name, next_places, start_text, other_text, enemies, searchable_objects, send_to_debris):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.next_places = next_places
        self.searchable_objects = searchable_objects
        self.start_text = start_text
        self.other_text = other_text
        self.enemies = enemies
        self.send_to_debris = send_to_debris

    def set_next_places(self, place_instances):
        self.next_places = place_instances

    def start(self):
        if self.send_to_debris:
            self.send_to_debris = False
            return True
        
        if self.name == "home":
            if True:
                print("well done brave traveller, you have won")
                print("game complete.")
        else:
            return self.do_something(self.start_text)
    
    def do_something(self, text): # I realise this is a bad name but this function just gets the user to do something
        choice = self.get_command(text)
        if isinstance(choice, Place):
            return choice
        if isinstance(choice, Enemy):
            battle(laika, choice)
            return self.do_something(self.other_text)
        choice.search()
        return self.do_something(self.other_text)

    def get_command(self, text):
        choices = {}
        for i in self.next_places:
            if not i[1]:
                choices[f"travel to {i[0].name}"] = i[0]
        for i in self.enemies:
            choices[f"fight {i.title}"] = i
        for i in self.searchable_objects:
            choices[f"search {i.name}"] = i

        command = inquirer.select(
            message=text,
            choices=list(choices.keys()),
        ).execute()
        return choices[command]

# defines all the places for the story
Home = Place("home", None, None, None, None, None, False)
Orbit = Place("orbit", [], "welcome to orbit, write some more stuff", "what else would you like to do in orbit", [test_goon], [test_closet], False)
Geostationary_Orbit = Place("geostationary orbit", [], "welcome to geostationary orbit, write some more stuff", "what else would you like to do in geostationary orbit", [], [], False)
Moon = Place("the Moon", [], "welcome to the Moon, write some more stuff", "what else would you like to do on the moon", [], [], False)
Mars = Place("Mars", [], "welcome to Mars, write some more stuff", "what else would you like to do on Mars", [], [], False)
Interstellar_Highway = Place("the interstellar highway", [], "welcome to the interstellar highway, write some more stuff", None, [], [], True)
Debris_Field = Place("the debris field", [], "welcome to the debris field, write some more stuff", "what else would you like to do in the debris field", [], [], False)
Jupiter = Place("Jupiter", [], "welcome to Jupiter, write some more stuff", "what else would you like to do on Jupiter",[], [], False)
Uranus = Place("Uranus", [], "welcome to Uranus, write some more stuff", "what else would you like to do on Uranus", [], [], False)
Strange_Space_Craft = Place("the strange space craft", [], "welcome to the strange space craft, write some more stuff", "what else would you like to do on the strange space craft", [], [], False)
Abyss = Place("the abyss", [], "welcome to the abyss, write some more stuff", "what else would you like to do in orbit", [], [], False)

# defines how the player can move between places in the story
Orbit.set_next_places([[Moon, True], [Geostationary_Orbit, True], [Mars, True], [Home, False]])
Geostationary_Orbit.set_next_places([[Mars, True], [Orbit, False]])
Moon.set_next_places([[Mars, True], [Orbit, False]])
Mars.set_next_places([[Interstellar_Highway, True], [Geostationary_Orbit, False], [Moon, False]])
Interstellar_Highway.set_next_places([[Orbit, False], [Geostationary_Orbit, False], [Moon, False], [Mars, False], [Debris_Field, False], [Jupiter, True], [Uranus, True], [Strange_Space_Craft, True], [Abyss, True]])
Jupiter.set_next_places([[Interstellar_Highway, False]])
Uranus.set_next_places([[Interstellar_Highway, False]])
Strange_Space_Craft.set_next_places([[Interstellar_Highway, False]])
Abyss.set_next_places([[Interstellar_Highway, False]])