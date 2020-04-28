import csv
import random

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
MAPS = {1: "map1.csv", 2: "map2.csv", 3:"map3.csv"}

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


def create_enemies(board, level_one_enemies=1, level_two_enemies=1, level_three_enemies=1):
    number_of_enemies = [level_one_enemies, level_two_enemies, level_three_enemies]
    enemy_name = [2, 3, 4]
    index = 1
    enemies = {}
    for number in range(len(number_of_enemies)):
        name = enemy_name[number]
        for enemy in range(number_of_enemies[number]):
            coordinates = get_random_coordinates(board)
            if name == enemy_name[0]:
                health = random.randint(1, 15)
                strength = random.randint(1, 15)
            elif name == enemy_name[1]:
                health = random.randint(15, 30)
                strength = random.randint(15, 30)
            else:
                health = random.randint(30, 50)
                strength = random.randint(30, 50)
            enemies[f"Enemy {index}"] = create_avatar_attributes(coordinates, name, health, strength)
            index += 1
        name += 1
    return enemies


def create_avatar_attributes(coordinates, name, health_points, strength_points, avatar_type="opponent"):
    pos_X, pos_Y = coordinates
    return {"pos_X": pos_X, "pos_Y": pos_Y, "name": name, "type": avatar_type, "helath": health_points, "strength": strength_points}


def get_random_coordinates(board):
    pos_X = random.randint(7, len(board) - 1)
    pos_Y = random.randint(7, len(board[0]) - 1)
    return pos_X, pos_Y


def move(direction, enitity):
    if direction == UP:
        enitity["pos_Y"] -= 1
    if direction == LEFT:
        enitity["pos_X"] -= 1
    if direction == DOWN:
        enitity["pos_Y"] += 1
    if direction == RIGHT:
        enitity["pos_X"] += 1


def move_in_direction(key, enitity):
    if key == 'w':
        move(UP, enitity)
    if key == 'a':
        move(LEFT, enitity)
    if key == 's':
        move(DOWN, enitity)
    if key == 'd':
        move(RIGHT, enitity)


def place_entitiy(board, enitity):
    x = enitity["pos_X"]
    y = enitity["pos_Y"]
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


def open_doors to another_level(level, board, pos_X, pos_Y):
    if board[pos_X][pos_Y] == "EX":
        level += 1
    elif board[pos_X][pos_Y] == "EN"
        level -= 1
    else:
        level = level
    return level