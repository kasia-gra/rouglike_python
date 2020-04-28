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
            util.clear_screen()
            ui.format(INVENTORY)
            back_to_game = input("Do you want to go back to game (Y/N) ?")
            if back_to_game == "Y":
                util.clear_screen()
        util.clear_screen()

if __name__ == "__main__":
    main()
