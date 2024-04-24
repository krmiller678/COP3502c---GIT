"""Tic Tac Toe Program"""
def print_board(board):
    '''
    :param board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ] 
    :return: None
    :print
    - - -
    - - -
    - - -
    '''
    for row in board:
        for element in row:
            print(element, end =" ")
        print()


def initialize_board():
    num_rows, num_cols = 3,3
    '''
    :return: board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ] 
    '''

    board = [
        ['-' for i in range(num_cols)]
        for j in range(num_rows)
    ]
    return board

def check_if_winner(board, chip_type):
    # check rows len(board) = 3 (number of rows)
    for row_index in range(len(board)):
        if board[row_index][0] == board[row_index][1] == board[row_index][2] == chip_type:
            return True
        
    # check columns: number of columns: len(board[0])
    for col_index in range(len(board[0])):
        if board[0][col_index] == board[1][col_index] == board[2][col_index] == chip_type:
            return True

    # diagonal
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
        return True
    
    if board[0][0] == board[1][1] == board[2][2] == chip_type:
        return True

def board_is_full(board):
    for row in board:
        for element in row:
            if element == '-':
                return False
    return True


def available_square(board, row, col):
    return board[row][col] == '-'


def mark_square(board, row, col, chip_type):
    board[row][col] = chip_type


def is_valid(board, row_index, col_index):
    return 0 <= row_index <= 2 and 0 <= col_index <= 2 and board[row_index][col_index] == '-'

def main():
    print("Player 1: x\nPlayer 2: o\n")

    board = initialize_board()
    print_board(board)
    print()

    player = 1
    chip = 'x'

    #Keep repeating this code snippet
    while True:
        print(f"Player {player}'s Turn ({chip}): ")

        row_index = int(input("Enter a row number (0, 1, or 2): "))
        col_index = int(input("Enter a column number (0, 1, or 2): "))


        while not is_valid(board, row_index, col_index):
            #giving error message
            if row_index < 0 or row_index > 2 or col_index < 0 or col_index >2:
                print("This position is off the bounds of the board! Try again.")
            elif board[row_index][col_index] != '-':
                print("Someone has already made a move at this position! Try again.")

            # keep asking the use to enter row_index and col_index
            row_index = int(input("Enter a row number (0, 1, or 2): "))
            col_index = int(input("Enter a column number (0, 1, or 2): "))

        if available_square(board, row_index, col_index):
            mark_square(board, row_index, col_index, chip)
            print_board(board)
            print()

            if check_if_winner(board, chip):
                print(f"Player {player} has won!")
                break
            elif board_is_full(board):
                print("It's a tie!")
                break

            player = 2 if player == 1 else 1
            chip = 'o' if chip == 'x' else 'x'


if __name__ == '__main__':
    main()