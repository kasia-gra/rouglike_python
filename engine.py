import csv
import random

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
WALL = "X"
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
        health, strength = get_health_and_strength(1, 15)
    elif name == ENEMY_NAMES[1]:
        health, strength = get_health_and_strength(15, 30)
    else:
        health, strength = get_health_and_strength(30, 50)
    return coordinates, health, strength


def get_random_coordinates(start_pos_X, start_pos_Y, board):
    enemy_player_distance_index_X = [index for index in range(start_pos_X - 3, start_pos_X + 4) if index >= 0]
    enemy_player_distance_index_Y = [index for index in range(start_pos_Y - 3, start_pos_Y + 4) if index >= 0]
    index_X = [index for index in range(len(board) - 1) if index not in enemy_player_distance_index_X]
    index_Y = [index for index in range(len(board) - 1) if index not in enemy_player_distance_index_Y]
    pos_X = random.choice(index_X)
    pos_Y = random.choice(index_Y)
    return pos_X, pos_Y


def get_health_and_strength(start_range, end_range):
    health = random.randint(start_range, end_range)
    strength = random.randint(start_range, end_range)
    return health, strength


def create_avatar_attributes(coordinates, name, health_points, strength_points, avatar_type="opponent"):
    pos_X, pos_Y = coordinates
    return {"pos_X": pos_X, "pos_Y": pos_Y, "name": name, "type": avatar_type, "helath": health_points, "strength": strength_points}


def get_coordinates(enitity):
    x = enitity["pos_X"]
    y = enitity["pos_Y"]
    return (x, y)

def clear_my_trace(board, enitity):
    (x,y) = get_coordinates(enitity)
    board[y][x] = ' '


def is_move_possible(enitity, elements_to_check, board, direction):
    x, y = get_coordinates(enitity)
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
    if board[y][x] == WALL:
        return False
    return True


def move(direction, enitity, board):
    clear_my_trace(board, enitity)
    if direction == UP:
        enitity["pos_Y"] -= 1
    if direction == LEFT:
        enitity["pos_X"] -= 1
    if direction == DOWN:
        enitity["pos_Y"] += 1
    if direction == RIGHT:
        enitity["pos_X"] += 1


def move_player(key, enitity, board):
    elements_to_check = [' ']
    if key == 'w' and is_move_possible(enitity, elements_to_check, board, UP):
        move(UP, enitity, board)
    if key == 'a' and is_move_possible(enitity, elements_to_check, board, LEFT):
        move(LEFT, enitity, board)
    if key == 's' and is_move_possible(enitity, elements_to_check, board, DOWN):
        move(DOWN, enitity, board)
    if key == 'd' and is_move_possible(enitity, elements_to_check, board, RIGHT):
        move(RIGHT, enitity, board)


def place_entitiy(board, enitity):
    (x, y) = get_coordinates(enitity)
    board[y][x] = enitity["name"]


def check_if_player_found_item(board, ITEMS, pos_X, pos_Y):
    has_found_item = False
    if board[pos_X][pos_Y] in ITEMS.keys():
        has_found_item = True
    return has_found_item


def add_item_to_inventory(INVENTORY, pos_X, pos_Y):
    item = board[pos_X][pos_Y]
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
