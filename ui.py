MAP_SCHEME = {'0': ' ', '1': '*', "@" : "@", "2": "<", "3": "&", "4": "%", "9": "[]"}



def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        for cell in row:
            print(MAP_SCHEME[cell], end='')
        print()
    print()
