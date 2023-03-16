    # Print the current state of the game board
def print_board():
    print("-------------")
    for i in range(ROWS):
        row = "| "
        for j in range(COLS):
            row += board[i][j] + " | "
        print(row)
        print("-----------------------------")


# Check if a player has won
def check_win(player):
    # Check rows
    for i in range(ROWS):
        for j in range(COLS - 3):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][
                j + 3] == player:
                return True
    # Check columns
    for i in range(ROWS - 3):
        for j in range(COLS):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][
                j] == player:
                return True
    # Check diagonals
    for i in range(ROWS - 3):
        for j in range(COLS - 3):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and \
                    board[i + 3][j + 3] == player:
                return True
            if board[i][j + 3] == player and board[i + 1][j + 2] == player and board[i + 2][j + 1] == player and \
                    board[i + 3][j] == player:
                return True
    return False


# Check if the game has ended in a draw
#def check_draw():
    # not yet implemented
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import random

    # Define the game board dimensions
    ROWS = 6
    COLS = 7

    # Define the players
    HUMAN = "X"
    COMPUTER = "O"

    # Initialize the game board
    board = [[" " for j in range(COLS)] for i in range(ROWS)]

    print_board()

    # get human move
    # check column not full
    # check for win or no more spaces left
    # make computer move
    # check for win or no more spaces left

    # Win end : congratulate winner
    # offer rematch






