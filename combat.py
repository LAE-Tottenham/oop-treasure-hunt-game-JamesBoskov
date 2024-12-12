import random
from misc_functions import *
from player import *
from enemy import *

#todo: enemies turn

def take_move(move, attacker, defender):
    if move["attack"]:    
        if move["power"] != 0:
            damage = (attacker.current_stats["attack"] + move["power"]) / defender.current_stats["defense"] + 2
        else:
            damage = 0
        if move["effect"][0] != None:
            defender.current_stats[move["effect"][0]] *= move["effect"][1]
        defender.current_stats["health"] -= damage
    else:
        attacker.current_stats[move["effect"][0]] *= move["effect"][1]

def combat_turn(player, enemy):
    # selects moves
    player_moves = []
    for i in player.moveset.values():
        player_moves.append(i["name"])
    player_move = player.moveset[check_valid_command(get_move_output(player), player_moves)]
    
    enemy_move = list(enemy.moveset.values())[random.randint(0, len(enemy.moveset.values())-1)]

    #completes turn
    if player.current_stats["speed"] > enemy.current_stats["speed"]:
        take_move(player_move, player, enemy)
        take_move(enemy_move, enemy, player)
    else:
        take_move(enemy_move, enemy, player)
        take_move(player_move, player, enemy)

combat_turn(laika, test_goon)
print(test_goon.current_stats, laika.current_stats)
