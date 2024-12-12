def check_valid_command(question, commands):
    while True:
        user_input = str(input(question))
        if user_input == "help":
            help(commands)
            continue
        if user_input in commands:
            return user_input
        print("That's not a valid command, remember typing help will give you a list of your possible commands.")

def help(commands):
    output = "Your valid commands are: "
    if len(commands) > 1:
        for i in range(len(commands)-1):
            output+=f"{commands[i]}, "
        output += f"and {commands[-1]}"
    else:
        output+=commands[0]
    print(output)

def get_move_output(player):
    move_names = "Choose your move:\n"
    for i in range(len(player.moveset.values())-1):
        move_names += f"{list(player.moveset.values())[i]["name"]}, "
    move_names += f"or {list(player.moveset.values())[-1]["name"]}\n"
    return move_names