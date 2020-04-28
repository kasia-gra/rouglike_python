import sys 
from termcolor import colored, cprint
import files_managment


ITEMS = files_managment.import_data_to_dict("items.csv")


MAP_SCHEME = {"@": "@", " ": " ", "X": colored("*"), "EX": colored("D", "white", "on_green"),\
              "EN": colored("D", "white", "on_yellow"),\
              "elixir": colored(ITEMS["elixir"]["name"], "magenta"), "key": colored(ITEMS["key"]["name"], "green"), "sword": colored(ITEMS["sword"]["name"], "yellow"),\
              "cloak": colored(ITEMS["cloak"]["name"], "blue"), "whip": colored(ITEMS["whip"]["name"], "yellow"), "2": "2", "3":"3", "4":"4"} 


def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        for cell in row:
            if cell not in MAP_SCHEME.keys():
                print(cell, end='')
            else:
                print(MAP_SCHEME[cell], end='')
        print()
    print()


def format(inventory):
    inventory = inventory.items()
    header1 = "item name"
    header2 = " count"
    mid = " |"
    left_padding = max([len(k) for k,v in inventory] + [len(header1)])
    right_padding = len(header2)
    mid_spacing = len(mid)
    total_padding = left_padding + right_padding + mid_spacing
    table_horizontal_border = (total_padding * "-").rjust(total_padding) + "\n"
    inventory_table = (table_horizontal_border +
                       header1.rjust(left_padding) + mid + header2.rjust(right_padding) +
                       "\n" + table_horizontal_border)
    for k,v in inventory:
        inventory_table = (inventory_table +
                           k.rjust(left_padding) + mid + f'{v}'.rjust(right_padding)
                           + "\n")
    print(inventory_table + table_horizontal_border)


def print_enemy(filename):
    with open(filename, "r") as file:
        enemy = file.read()
        print(enemy)


def print_game_statistics(player, enemies, name):
    atributes_to_print = ["strength", "helath"]
    for k,v in enemies.items():
        if v["name"] == name:
            enemies = v
    statistics = zip(player.items(), enemies.items())
    game_stat_formatted = (f"Player statistics              Enemy statistics\n")
    for item in statistics:
        if item[0][0] in atributes_to_print:
            game_stat_formatted += (f"{item[0][0]} {item[0][1]}                      {item[1][0]} {item[1][1]}")
            game_stat_formatted += "\n"
    print(game_stat_formatted)