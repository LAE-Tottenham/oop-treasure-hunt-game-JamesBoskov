from misc_functions import *
from player import *
from enemy import *

#todo: enemies turn

def combat_turn(player, enemy):
    #takes in players move selection
    player_moves = []
    for i in player.moveset.values():
        player_moves.append(i["name"])
    player_move = player.moveset[check_valid_command(get_move_output(player), player_moves)]
    print(player_move, enemy.current_stats)
    
    #completes player's turn
    if player_move["attack"]:    
        if player_move["power"] != 0:
            damage = (player.current_stats["attack"] + player_move["power"]) / enemy.current_stats["defense"] + 2
        else:
            damage = 0
        if player_move["effect"][0] != None:
            enemy.current_stats[player_move["effect"][0]] *= player_move["effect"][1]
    else:
        player.current_stats[player_move["effect"][0]] *= player_move["effect"][1]
    


    enemy.current_stats["health"] -= damage
    print(enemy.current_stats)

combat_turn(laika, test_goon)
print(test_goon.current_stats)