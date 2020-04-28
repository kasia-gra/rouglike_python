import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


ENEMY1 = "2"
ENEMY2 = "3"
ENEMY3 = "4"
INVENTORY = {}


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
    board = engine.create_board(level)
    enemies = engine.create_enemies(PLAYER_START_X, PLAYER_START_Y, board, 3)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.place_entitiy(board, player)
        for key, value in enemies.items():
            engine.place_entitiy(board, value)
        ui.display_board(board)
        key = util.key_pressed()
        engine.move_player(key, player, board)
        if key == 'q':
            is_running = False
        elif key == "i":
            chagne_mode_from_game_to_inventory(INVENTORY)
        util.clear_screen()

if __name__ == "__main__":
    main()
