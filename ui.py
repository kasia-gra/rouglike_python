import sys 
from termcolor import colored, cprint


ITEMS  = {"sword": {"name": "S", "type": "weapon", "strenght": 20, "health": 0},\
        "whip": {"name": "W", "type": "weapon", "strenght": 10, "health": 0},\
        "elixir": {"name": "E", "type": "potions", "strenght": 5, "health": 10},\
        "cloak": {"name": "C", "type": "magic_item", "strenght": 5, "health": 5},\
        "key": {"name": "K", "type": "magic_item", "strenght": 0, "health": 0}}


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