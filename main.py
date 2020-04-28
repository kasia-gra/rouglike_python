import util
import engine
import ui
import random

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

INVENTORY = {}
NUMBER_OF_MAPS = 3


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    health = 40
    strength = 10
    player = engine.create_avatar_attributes((PLAYER_START_X, PLAYER_START_Y), PLAYER_ICON, health, strength, "player")
    return player


def chagne_mode_from_game_to_inventory(INVENTORY):
    while True:
        try: 
            ui.format(INVENTORY)
            back_to_game = input("Type 'y' if you want to go back to game")
            if back_to_game == "y":
                util.clear_screen()
                break
            else:
                raise ValueError
        except ValueError:
            print("ooops you need to press 'y' to go back to game")


def main():
    level = 1
    player = create_player()
    maps = generate_maps()
    enemies = generate_enemies(maps)
    util.clear_screen()
    is_running = True
    while is_running:
        board = switch_map(level, maps)
        engine.place_entitiy(board, player)
        for key, value in enemies[level - 1].items():
            engine.place_entitiy(board, value)
        ui.display_board(board)
        key = util.key_pressed()
        engine.move_player(key, player, board)
        if key in "wsad":
            for enemy_key, value in enemies[level - 1].items():
                engine.move_player(random.choice(["w", "s", "a", "d"]), value, board)
        elif key == 'q':
            is_running = False
        elif key == "i":
            chagne_mode_from_game_to_inventory(INVENTORY)
        util.clear_screen()


def generate_maps():
    maps = []
    for index in range(NUMBER_OF_MAPS):
        maps.append(engine.create_board(index + 1))
    return maps


def generate_enemies(maps):
    enemies = []
    for index in range(NUMBER_OF_MAPS):
        enemies.append(engine.create_enemies(PLAYER_START_X, PLAYER_START_Y, maps[index], 3))
    return enemies


def switch_map(level, maps):
    return maps[level - 1]


if __name__ == "__main__":
    main()
