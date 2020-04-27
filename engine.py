import csv


def create_board(width, height):
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


def create_avatar_attributes(coordinates, name, health_points, strength_points, avatar_type="opponent"):
    pos_X, pos_Y = coordinates
    return {"pos_X": pos_X, "pos_Y": pos_Y, "name": name, "type": avatar_type, "helath": health_points, "strength": strength_points}


def create_enemies(level_one_enemies=1, level_two_enemies=1, level_three_enemies=1):
    number_of_enemies = [level_one_enemies, level_two_enemies, level_three_enemies]
    name = 2
    index = 1
    enemies = {}
    for number in range(len(number_of_enemies)):
        for enemy in range(number_of_enemies[number]):
            coordinates = (0, 0) # get_random_coordinates() will be implemented
            if name == 2:
                health = 10
                strength = 10
            elif name == 3:
                health = 25
                strength = 20
            else:
                health = 35
                strength = 25
            enemies[f"ENEMY{index}"] = create_avatar_attributes(coordinates, name, health, strength)
            index += 1
        name += 1
    return enemies
