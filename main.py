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
            print("Type 'y' if you want to go back to game or 'q' for quit game")
            key_presed = util.key_pressed()
            if key_presed == "y":
                util.clear_screen()
                break
            elif key_presed == 'q':
                exit()
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
    exit_doors_statuses = generate_doors_status_and_position(maps)
    util.clear_screen()
    is_running = True
    while is_running:
        board = switch_map(level, maps)
        place_players_on_board(board, player, enemies, level)
        ui.display_board(board)
        ui.display_avatar_atributes(player, FIGHT_ATRIBUTES)
        key = util.key_pressed()
        engine.move_player(key, player, board, exit_doors_statuses, level)
        player_next_step = engine.get_player_next_step(player, board)
        level, exit_doors_statuses = handle_player_next_step(player_next_step, player, enemies[level - 1], level, exit_doors_statuses)
        handle_key_pressed(key, enemies, level, player_inventory, board, exit_doors_statuses)
        engine.check_player_enemies_position(player, enemies[level - 1])
        delete_defeted_enemy_from_board(enemies, level)
        util.clear_screen()


def place_players_on_board(board, player, enemies, level):
    engine.place_entitiy(board, player)
    for key, value in enemies[level - 1].items():
        engine.place_entitiy(board, value)


def handle_player_next_step(player_next_step, player, enemies, level, exit_doors_statuses):
    if player_next_step == "EX" or player_next_step == "EN":
            level, exit_doors_statuses = engine.use_doors(player_next_step, level, player, exit_doors_statuses)
    elif player_next_step in "2348":
        engine.check_player_enemies_position(player, enemies)
    elif player_next_step in ui.ITEMS:
        engine.collect_item(player_next_step, ui.ITEMS, player)
        player_inventory = player["inventory"]
        for fight_atribute in FIGHT_ATRIBUTES:
            player[fight_atribute] += int(ui.ITEMS[player_next_step][fight_atribute])
    return level, exit_doors_statuses

def handle_key_pressed(key, enemies, level, player_inventory, board, exit_doors_statuses):
    if key in "wsad":
        for enemy_key, value in enemies[level - 1].items():
            engine.move_player(random.choice(["w", "s", "a", "d"]), value, board, exit_doors_statuses, level)
    elif key == 'q':
        is_running = False
    elif key == "i":
        chagne_mode_from_game_to_inventory(player_inventory)


def delete_defeted_enemy_from_board(enemies, level):
    key_to_delete = engine.generate_enemy_key_to_delete(enemies[level - 1])
    if key_to_delete is not None:
        del enemies[level - 1][key_to_delete]


def generate_maps():
    maps = []
    for index in range(NUMBER_OF_MAPS):
        maps.append(engine.create_board(index + 1))
    return maps


def generate_enemies(maps):
    enemies = []
    for index in range(NUMBER_OF_MAPS):
        single_map_enemies = engine.create_enemies(PLAYER_START_X, PLAYER_START_Y, maps[index], 3)
        enemies.append(single_map_enemies)
    # add_boss = enemies[1]
    # add_boss["Boss"] = engine.create_boss(1, 27, add_boss)
    return enemies


def switch_map(level, maps):
    engine.clear_board_from_enemies(maps[level - 1])
    return maps[level - 1]

def generate_doors_status_and_position(maps):
    exit_doors_statuses = {}
    for index in range(NUMBER_OF_MAPS):
        single_doors_dictionary = {}
        for map_row_index in range(len(maps[index])):
            if "EX" in maps[index][map_row_index]:
                EX_doors_pos_y = map_row_index + 1
                EX_doors_pos_X = maps[index][map_row_index].index("EX") + 1
                single_doors_dictionary["doors_position"] = (EX_doors_pos_X, EX_doors_pos_y)  
                single_doors_dictionary["status"] = "closed"
        exit_doors_statuses[index + 1] = single_doors_dictionary
    return exit_doors_statuses

if __name__ == "__main__":
    main()