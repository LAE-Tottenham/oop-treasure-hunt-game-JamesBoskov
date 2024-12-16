import random
from misc_functions import *
from player import *
from enemy import *
from item import *
import copy
import os

def show_health(player, enemy):
    print(f"Laika: {player.current_stats["health"]}hp\n{enemy.name}: {enemy.current_stats["health"]}hp")

def effect(move, defender):
    if move.effect[0] != "health":
        defender.current_stats[move.effect[0]] *= move.effect[1]
        if move.effect[1] > 1:
            print(f"{defender.name}'s {move.effect[0]} was increased")
        else:
            print(f"{defender.name}'s {move.effect[0]} was decreased")
    else:
        defender.current_stats[move.effect[0]] += move.effect[1]
        print(f"{defender.name}'s health was increased by {move.effect[1]}")

def take_move(move, attacker, defender):
    if move.attack:    
        if move.power != 0:
            damage = int((attacker.current_stats["attack"] + move.power) / defender.current_stats["defense"] + 2)
            print(f"{attacker.name} used {move.name} and dealt {damage} damage")
        else:
            damage = 0
        if move.effect[0] != None:
            effect(move, defender)
        defender.current_stats["health"] -= damage
    else:
        effect(move, attacker)

    if defender.current_stats["health"] <= 0:
        return True

def move(player, enemy):
    # selects moves
    player_moves = []
    for i in player.moveset:
        player_moves.append(i.name)
    player_move_name = check_valid_command(get_move_output(player), player_moves)
    for i in player.moveset:
        if i.name == player_move_name:
            player_move = i

    os.system("clear")
    enemy_move = enemy.moveset[random.randint(0, len(enemy.moveset)-1)]

    #completes turn
    if player.current_stats["speed"] > enemy.current_stats["speed"]:
        dead = take_move(player_move, player, enemy)
        if dead:
            return True
        dead = take_move(enemy_move, enemy, player)
        if dead:
            return False
    else:
        dead = take_move(enemy_move, enemy, player)
        if dead:
            return True 
        take_move(player_move, player, enemy)
        if dead:
            return False
    show_health(player, enemy)
    return None

def use_item(player, enemy):
    if player.items == []:
        print("You have no items to use, lets try that again.")
        return combat_turn(player, enemy)
    player_items = []
    for i in player.items:
        player_items.append(i.name)
    player_item_name = check_valid_command(get_item_output(player), player_items)
    for i in player.items:
        if i.name == player_item_name:
            player_item = i
    effect(player_item, player)
    player.items.remove(player_item)

    # print some stuff
    print(f"Laika used {player_item_name}")
    os.system("clear")
    if player_item.effect[0] == "health":
        print(f"Laika increased her health by {player_item.effect[1]}")
    else:
        print(f"Laika increased her {player_item.effect[0]}")

    enemy_move = enemy.moveset[random.randint(0, len(enemy.moveset)-1)]
    dead = take_move(enemy_move, enemy, player)
    show_health(player, enemy)
    if dead:
        return False
    return None

def combat_turn(player, enemy):
    item_or_move = check_valid_command("Would you like to use an item or use a move: ", ["use an item", "item", "use a move", "move"])
    if item_or_move == "use an item" or item_or_move == "item":
        return use_item(player, enemy)
    else:
        return move(player, enemy)

def battle(player, enemy):
    os.system("clear")
    while True:
        turn_result = combat_turn(player, enemy)
        if turn_result:
            print(f"{enemy.name} has exploded into millions of bits, well done.")
            break
        if turn_result == False:
            print(turn_result)
            print("kaboom, with one final blow Laika is propelled into the cosmos by a ruch of air, try again.")
            player.place = copy.deepcopy(player.checkpoint)
            break

laika.items.append(blowtorch)
battle(laika, test_goon)
print(test_goon.current_stats, laika.current_stats)