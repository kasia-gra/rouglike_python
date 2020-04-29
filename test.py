import random


row = [" "] * 10
board = [row] * 10

def get_random_coordinates( board, start_pos_X = 3, start_pos_Y = 3):
    enemy_player_distance_index_X = [index for index in range(start_pos_X - 3, start_pos_X + 4) if index >= 0]
    enemy_player_distance_index_Y = [index for index in range(start_pos_Y - 3, start_pos_Y + 4) if index >= 0]
    index_X = [index for index in range(len(board) - 1) if index not in enemy_player_distance_index_X]
    index_Y = [index for index in range(len(board) - 1) if index not in enemy_player_distance_index_Y]
    check_coordinates = True
    while check_coordinates:
        pos_X = random.choice(index_X)
        pos_Y = random.choice(index_Y)
        if check_random_coordinates(pos_X, pos_Y, board):
            check_coordinates = False
    return pos_X, pos_Y


def check_random_coordinates(pos_X, pos_Y, board):
    return board[pos_X][pos_Y] == " "

print(get_random_coordinates(board))