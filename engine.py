import csv
import random


def create_board():
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    with open("map1.csv", "r") as file:
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
