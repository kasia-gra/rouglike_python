import csv
import random
import os
import time
import util
import ui
import files_managment


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
WALL = "X"
ATTACK = "k"
DEFFENCE = "l"
MAPS = {1: "map1.csv", 2: "map2.csv", 3:"map3.csv"}
DOORS = {"EX": {"name": "X", "status": "closed"},
          "EN": {"name": "N", "status": "open"}}
ENEMY_NAMES = ["2", "3", "4"]


def create_board(level):
    '''
    Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    '''

    with open(MAPS[level], "r") as file:
        board = csv.reader(file)
        return list(board)


def update_board(level, board):
    with open(MAPS[level], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(board)

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.
    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates
    Returns:
    Nothing
    '''
    pass


def create_enemies(player_start_pos_X, player_start_pos_Y, board, number_of_enemies=1):
    number_of_enemies = generate_enemies_on_all_levels(number_of_enemies)
    enemies = {}
    for index, number in enumerate(number_of_enemies, start=1):
        name = number
        for enemy in range(len(number_of_enemies)):
            coordinates, health, strength = generate_single_level_enemy(name,player_start_pos_X, player_start_pos_Y, board)
            enemies[f"Enemy {index}"] = create_avatar_attributes(coordinates, name, health, strength)
    return enemies


def generate_enemies_on_all_levels(number_of_enemies):
    enemies = []
    for element in range(number_of_enemies):
        enemies.append(random.choice(ENEMY_NAMES))
    return enemies


def generate_single_level_enemy(name, player_start_pos_X, player_start_pos_Y, board):
    coordinates = get_random_coordinates(player_start_pos_X, player_start_pos_Y, board)
    if name == ENEMY_NAMES[0]:
        health, strength = get_health_and_strength(1, 7)
    elif name == ENEMY_NAMES[1]:
        health, strength = get_health_and_strength(8, 15)
    else:
        health, strength = get_health_and_strength(15, 25)
    return coordinates, health, strength


def get_random_coordinates(start_pos_X, start_pos_Y, board):
    enemy_player_distance_index_X = [index for index in range(start_pos_X - 3, start_pos_X + 4) if index > 0]
    enemy_player_distance_index_Y = [index for index in range(start_pos_Y - 3, start_pos_Y + 4) if index > 0]
    index_X = [index for index in range(len(board) - 2) if index not in enemy_player_distance_index_X]
    index_Y = [index for index in range(len(board) - 2) if index not in enemy_player_distance_index_Y]
    check_coordinates = True
    while check_coordinates:
        pos_X = random.choice(index_X)
        pos_Y = random.choice(index_Y)
        if check_random_coordinates(pos_X, pos_Y, board):
            check_coordinates = False
    return pos_X, pos_Y


def check_random_coordinates(pos_X, pos_Y, board):
    return board[pos_X][pos_Y] == " " or board[pos_X][pos_Y] == "@"


def get_health_and_strength(start_range, end_range):
    health = random.randint(start_range, end_range)
    strength = random.randint(start_range, end_range)
    return health, strength


def create_avatar_attributes(coordinates, name, health_points, strength_points, avatar_type="opponent"):
    pos_X, pos_Y = coordinates
    return {"pos_X": pos_X, "pos_Y": pos_Y, "name": name, "type": avatar_type, "health": health_points, "strength": strength_points, "file name": f"enemy{name}.txt"}


def get_coordinates(entity):
    x = entity["pos_X"]
    y = entity["pos_Y"]
    return (x, y)

def clear_my_trace(board, entity):
    (x,y) = get_coordinates(entity)
    board[y][x] = ' '


def is_move_possible(entity, elements_to_check, board, direction):
    x, y = get_coordinates(entity)
    if direction == UP:
        direction_to_check = (x, y-1)
    if direction == LEFT:
        direction_to_check = (x-1, y)
    if direction == DOWN:
        direction_to_check = (x, y+1)
    if direction == RIGHT:
        direction_to_check = (x+1, y)
    
    x = direction_to_check[0]
    y = direction_to_check[1]
    # if board[y][x] not in elements_to_check:
    if entity["name"] in "234":
        if board[y][x] in [WALL, "EX", "EN", "elixir", "key", "sword", "cloak", "whip", "2", "3", "4"]:
            return False
    if board[y][x] == WALL:
        return False
    return True


def mark_new_coordinates(entity, coordinates):
    x, y = coordinates
    entity["pos_X"] = x
    entity["pos_Y"] = y


def get_character_in_position(x, y, board):
    return board[y][x]


def get_player_next_step(player, board):
    x, y = get_coordinates(player)
    player_next_step = get_character_in_position(x, y, board)
    return player_next_step


def use_doors(player_next_step, level, player):
    player_default_coordinates = (3, 3)
    if player_next_step == "EX":
        level += 1
    elif player_next_step == "EN":
        level -= 1
    mark_new_coordinates(player, player_default_coordinates)
    return level


def collect_item(player_next_step, ITEMS, player):
    player["inventory"] = add_item_to_inventory(player["inventory"], player_next_step)


def move(direction, entity, board):
    clear_my_trace(board, entity)
    if direction == UP:
        entity["pos_Y"] -= 1
    if direction == LEFT:
        entity["pos_X"] -= 1
    if direction == DOWN:
        entity["pos_Y"] += 1
    if direction == RIGHT:
        entity["pos_X"] += 1


def move_player(key, entity, board):
    elements_to_check = [' ']
    if key == 'w' and is_move_possible(entity, elements_to_check, board, UP):
        move(UP, entity, board)
    if key == 'a' and is_move_possible(entity, elements_to_check, board, LEFT):
        move(LEFT, entity, board)
    if key == 's' and is_move_possible(entity, elements_to_check, board, DOWN):
        move(DOWN, entity, board)
    if key == 'd' and is_move_possible(entity, elements_to_check, board, RIGHT):
        move(RIGHT, entity, board)


def place_entitiy(board, entity):
    (x, y) = get_coordinates(entity)
    board[y][x] = entity["name"]


# def check_if_player_found_item(board, ITEMS, pos_X, pos_Y):
#     has_found_item = False
#     if board[pos_X][pos_Y] in ITEMS.keys():
#         has_found_item = True
#     return has_found_item


def add_item_to_inventory(INVENTORY, item):
    if item in INVENTORY:
        INVENTORY[item] += 1
    else:
        INVENTORY[item] = 1
    return INVENTORY


def remove_from_inventory(INVENTORY, item):
    INVENTORY[item] -= 1
    return INVENTORY


def go_to_another_level(level, board, player, DOORS):
    pos_X, pos_Y = get_coordinates(player)
    if board[pos_X][pos_Y] == "EX" and DOORS["status"] == "open":
        level += 1
    elif board[pos_X][pos_Y] == "EN":
        level -= 1
    else:
        level = level
    return level


def choose_avatar(DIRPATH, FIGHT_ATRIBUTES):
    avatars_atributes = files_managment.import_data_to_dict(DIRPATH, "avatars_files", "avatars_atributes.csv")
    avatar_chosen = False
    avatar_index = 0
    all_avatars = list(avatars_atributes.keys())
    while not avatar_chosen:
        print("\nUse keys 's' and 'd' to view avatars. To choose avatar press space button")
        key = util.key_pressed()
        if key == "d" and avatar_index != len(all_avatars)-1:
            avatar_index += 1
        elif key == "d" and avatar_index == len(all_avatars)-1:
            avatar_index = 0
        elif key == "s" and avatar_index != 0:
            avatar_index -= 1
        elif key == "s" and avatar_index == 0:
            avatar_index = len(all_avatars) - 1
        elif key == " ":
            print(f"Your avatar is {all_avatars[avatar_index].upper()}")
            time.sleep(1)
            avatar_chosen = True
        else:
            pass
        os.system("clear")
        ui.print_avatar(DIRPATH, avatar_index, FIGHT_ATRIBUTES)
        print(avatars_atributes[all_avatars[avatar_index]])
    return avatars_atributes[all_avatars[avatar_index]]


def enemy_encounter(player_dict, enemy_dict):
    fight_in_progress = True
    print(f'Player strength: {player_dict["strength"]}     Enemy strength: {enemy_dict["strength"]}')
    while fight_in_progress:
        single_player_power = get_avatar_single_move_power(player_dict["strength"])
        single_enemy_power = get_avatar_single_move_power(enemy_dict["strength"])
        enemy_move = random.choice([ATTACK, DEFFENCE])
        avatar_move = util.key_pressed()
        if avatar_move == ATTACK or avatar_move == DEFFENCE:
            result = get_encounter_result(avatar_move, enemy_move, player_dict, enemy_dict, single_player_power, single_enemy_power)
            print('player health: %.2f        Enemy health: %.2f' % (player_dict["health"], enemy_dict["health"]))
            if player_dict["health"] <= 0:
                util.clear_screen()
                print("GAME OVER\nYou loose!")
                exit()
            elif enemy_dict["health"] <= 0:
                print("Enemy defeated!")
                time.sleep(1)
                fight_in_progress = False


def get_encounter_result(avatar_move, enemy_move, player_dict, enemy_dict, single_player_power, single_enemy_power):
    if avatar_move == ATTACK and enemy_move == ATTACK:
        player_dict["health"] = player_dict["health"] - single_enemy_power
        enemy_dict["health"] = enemy_dict["health"] - single_player_power
        comment = "Players attack each other"
    elif avatar_move == ATTACK and enemy_move == DEFFENCE:
        enemy_defence = single_player_power - single_enemy_power
        if enemy_defence <= 0:
            enemy_defence = 0
        enemy_dict["health"] = enemy_dict["health"] - enemy_defence
        comment = f"Enemy partially block your attack"
    elif avatar_move == DEFFENCE and enemy_move == ATTACK:
        player_defence = single_enemy_power - single_player_power
        if player_defence <= 0:
            player_defence = 0
        player_dict["health"] = player_dict["health"] - player_defence
        comment = "You partially block enemy attack"
    elif avatar_move == DEFFENCE and enemy_move == DEFFENCE:
        comment = "Players block each other"
    else:
        comment = ""
    return comment


def get_avatar_single_move_power(strength):
    single_move_power = 0
    if strength in range(1, 15):
        single_move_power = random.choice([3.55, 3.6, 3.65])
    elif strength in range(15, 30):
        single_move_power = random.choice([3.7, 3.75, 3.8])
    elif strength > 30:
        single_move_power = random.choice([3.85, 3.9, 3.95])
    return single_move_power


def check_player_enemies_position(player, enemies):
    for enemy_key, value in enemies.items():
        if value["pos_X"] == player["pos_X"] and value["pos_Y"] == player["pos_Y"]:
            util.clear_screen()
            ui.print_enemy(value["file name"])
            print(f"Attack --> k    Defence --> l")
            enemy_encounter(player, value)


def generate_enemy_key_to_delete(enemies):
    for key, value in enemies.items():
        for value_key, enemy_value in value.items():
            if value_key == "health":
                if enemy_value <= 0:
                    return key


def clear_board_from_enemies(board):
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if board[row_index][column_index] in "234":
                board[row_index][column_index] = " "
    return board
