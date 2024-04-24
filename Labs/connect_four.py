"""Lab 5: Connect-Four"""

# Define program methods
def print_board(board):
    """
    Print the board element by element, each row is new line
    """
    #No return, but for each row print each element
    for row in board:
        for element in row:
            print(element, end = ' ')
        print()


def initialize_board(num_rows,num_cols):
    """
    :return: board as 2D list
    """
    #set board to create 2D list with cols in each row for each row
    board = [
        ['-' for i in range(num_cols)]
        for j in range(num_rows)
        ]
    return board


def insert_chip(board, col, chip_type):
    """
    Establish highest value row with free space for chip to fall in
    """
    #establish free space in highest index row
    for i in range(len(board)):
        if board[len(board)-1-i][col] == '-':
            board_height = len(board) - 1- i
            break

    board[board_height][col] = chip_type

    return board_height


def check_if_winner(board, col, row, chip_type):
    """
    Check row for 4 in a row
    Check col for 4 in a col
    """
    return_value = False
    
    #check row
    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
        else:
            count = 0
        if count == 4:
            return_value = True

    #check col
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
        else:
            count = 0
        if count == 4:
            return_value = True

    return return_value


def main():
    #First step - Gather user input:
    rows = int(input('What would you like the height of the board to be? '))
    cols = int(input('What would you like the length of the board to be? '))

    board = initialize_board(rows,cols)
    print_board(board)
    print()
    print("Player 1: x\nPlayer 2: o\n")

    player = 1
    chip = 'x'

    #Keep repeating this loop until someone wins or tie
    while True:
        col = int(input(f"Player {player}: Which column would you like to choose? "))
        row = insert_chip(board, col, chip)
        print_board(board)

        #check for winner
        if check_if_winner(board, col, row, chip):
            print(f"Player {player} won the game!")
            break

        #check to make sure there is still space left
        space_left = False
        for i in board[0]:
            if i == '-':
                space_left = True
                break
        
        if space_left == False:
            print("Draw. Nobody wins.")
            break


        player = 2 if player == 1 else 1
        chip = 'o' if chip == 'x' else 'x'


if __name__ == '__main__':
    main()