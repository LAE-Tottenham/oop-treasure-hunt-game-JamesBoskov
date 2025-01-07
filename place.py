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
                laika.proggress += 1
                laika.stats["health"] += 2
                laika.stats["attack"] += 2
                laika.stats["speed"] += 2
                laika.stats["defense"] += 2
                if laika.proggress in list(proggression_moves.keys()):
                    print(f"laika learnt {proggression_moves[laika.proggress]}")
                    laika.moveset.append(proggression_moves[laika.proggress])
                if laika.proggress == 9:
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
Orbit = Place("orbit", [], "Welcome to orbit, you are currently circling around the earth at a speed of seven and a half kilometres a second. You may be alone in the vast expanse of space, but you do have some ideas as to what you want to do. You could: ", "What next?",
               [space_rock], [comet, meteor], "Well done on pulverising that murderous peice of nickel, in the ensueing cloud of smoke you managed to find your rocket's fins, in the words of Borat, 'great success'", 
               False, False)

Geostationary_Orbit = Place("geostationary orbit", [], "Welcome to geostationary orbit, you are now circling the earth at over 35000km, this allows you to be above the same place on earth at all times, not that you care. Where will your whim carry you next?",
                             "Anything else?", [ominous_sattelite], [derelict_sattelite, abandoned_space_station], "You have majorly destroyed that pesky satelite. Coincidentally you managed to find your nose cone in the wreck, or maybe it isn't yours, don't know don't care",
                               False, False)

Moon = Place("the Moon", [], "Welcome to the Moon, as you land on its surface you feel the ship get stuck to something sticky, as you walk out you fin a mess of gooey cheese beneath your feet, what do you do next?",
              "Any other moonish errands need running?", [cheese_monster], [cheese_shop, cheese_shop2], "You wade through the sticky, melty mess he left behind, and just in the centre you find it, your rocket's central computer.", False, False)

Mars = Place("Mars", [], "welcome to Mars, you are far away from home now, and its just now setting in, but if you want to succeed you'll have to push that feeling of fear down and keep trudging on", 
             "Bet you were expecting a martian, take that. Anything else while your here?", [rex], [], "You tear down the final frontier of capitalism, space. A prideful tear wells up inside you as you retrieve your parachute.", False, False)

Interstellar_Highway = Place("the interstellar highway", [], "welcome to the interstellar highway, where to?", None, [], [], "", True)

Debris_Field = Place("the debris field", [], "On your way to the interstellar highway youv'e been lead of course and are now blocked in a giant field of floating space debris by a strange ship.", "Descisions, desiscions.", [strange_ship], [abandoned_craft, abandoned_craft2],
                      "Youv'e defeated this oddity, although you still feel uneasy about the whole affair.")

Jupiter = Place("Jupiter", [], "welcome to Jupiter, this gas giant is the biggest in our solar system, its clouds of gas have been said to hide things well",
                 "What else would you like to do on Jupiter?",[jovian], [jovian_surface], "You kill this thing, it cries in anguish. However you did manage to recover your guidance sensors so pros and cons i guess.")

Uranus = Place("Uranus", [], "welcome to Uranus, it can get cold here, -195 degrees celsius. You hope your thermal insulation is still functional after the crash.",
                "What else would you like to do on Uranus?", [uranian], [uranian_surface], "It's screams will haunt you for weaks, but having your capsules flotaion devices will making landing in the sea alot more survivable.")

Strange_Space_Craft = Place("the strange space craft", [], "welcome to the strange space craft, the aliens aboard are not unlike your friends from back home, but they stare at you strangely and piercingly.",
                             "What else would you like to do here?", [alien_warrior], [], "It lies at your feet, slain. Well done, you salvage your rockets nozzle, one more step left.")

Abyss = Place("the abyss", [], "You float, alone, through an unending abyss. Another ship now joins you, maybe this is the way out", "Leave this place and cleanse it from your memory.", [zorgul], [], "Finally, its over, this journey these battles, youve done the hard part, now get back home. You find the bolts needed to fit all the peices youve collected together.")

# defines how the player can move between places in the story
Orbit.set_next_places([Moon, Geostationary_Orbit, Mars, Home, Interstellar_Highway])
Geostationary_Orbit.set_next_places([Orbit, Mars])
Moon.set_next_places([Mars, Orbit])
Mars.set_next_places([Interstellar_Highway, Geostationary_Orbit, Moon])
Interstellar_Highway.set_next_places([Orbit, Geostationary_Orbit, Moon, Mars, Debris_Field, Jupiter, Uranus, Strange_Space_Craft])
Jupiter.set_next_places([Interstellar_Highway])
Uranus.set_next_places([Interstellar_Highway])
Strange_Space_Craft.set_next_places([Interstellar_Highway, Strange_Space_Craft])
Abyss.set_next_places([Strange_Space_Craft])
places = [Orbit, Geostationary_Orbit, Moon, Mars, Interstellar_Highway, Jupiter, Uranus, Strange_Space_Craft, Abyss]