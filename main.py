import util
import engine
import ui
import random
import os
import files_managment


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
FIGHT_ATRIBUTES = ["health", "strength"]

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

NUMBER_OF_MAPS = 3
DIRPATH = os.getcwd()

# def create_player():
#     '''
#     Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
#     Fell free to extend this dictionary!
#     Returns:
#     dictionary
#     '''
#     health = 40
#     strength = 10
#     player = engine.create_avatar_attributes((PLAYER_START_X, PLAYER_START_Y), PLAYER_ICON, health, strength, "player")
#     player["inventory"] = {}
#     return player


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
    player_inventory = {}
    # player = create_player()
    player = engine.choose_avatar(DIRPATH, FIGHT_ATRIBUTES)
    player["inventory"] = {}
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
        print(player_inventory)
        print(player)
        key = util.key_pressed()
        engine.move_player(key, player, board)
        player_next_step = engine.get_player_next_step(player, board)
        if player_next_step == "EX" or player_next_step == "EN":
            level = engine.use_doors(player_next_step, level, player)
        elif player_next_step in ui.ITEMS:
            engine.collect_item(player_next_step, ui.ITEMS, player)
            player_inventory = player["inventory"]
            for fight_atribute in FIGHT_ATRIBUTES:
                player[fight_atribute] += int(ui.ITEMS[player_next_step][fight_atribute])
        if key in "wsad":
            for enemy_key, value in enemies[level - 1].items():
                engine.move_player(random.choice(["w", "s", "a", "d"]), value, board)
        elif key == 'q':
            is_running = False
        elif key == "i":
            chagne_mode_from_game_to_inventory(player_inventory)
        engine.check_player_enemies_position(player, enemies[level - 1])
        key_to_delete = engine.generate_enemy_key_to_delete(enemies[level - 1])
        if key_to_delete is not None:
            del enemies[level - 1][key_to_delete]
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