    # Print the current state of the game board
def print_board():
    print("-------------")
    for the_c in range(my_COLS):
        #print("the c is:", the_c)
        row = "| "
        for the_r in range(my_ROWS):
            #print("the r is :", the_r)
            row += board[the_c][the_r] + " | "
        print(row)
        print("-----------------------------")

#Put the correct symbol in the correct column
def print_symbol(symbol, column):
    print(board[column])
    for the_r in range(my_ROWS, 0, -1):
        if board[column][the_r] == " ":
            board[column][the_r] = symbol
            #print("debug")
            break


# Check if a player has won
def check_win(player):
    # Check rows
    for the_c in range(my_COLS):
        for the_r in range(my_ROWS - 3):
            if board[the_c][the_r] == player and board[the_c][the_r + 1] == player and board[the_c][the_r + 2] == player and board[the_c][
                the_r + 3] == player:
                return True
    # Check columns
    for i in range(my_COLS - 3):
        for j in range(my_ROWS):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][
                j] == player:
                return True
    # Check diagonals
    for i in range(my_COLS - 3):
        for j in range(my_ROWS - 3):
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
    my_COLS = 7
    my_ROWS = 2

    # Define the players
    HUMAN = "X"
    COMPUTER = "O"

    board = [[(' ') for the_c in range(my_COLS)] for the_r in range(my_ROWS)]

    print_board()
#game in progress
    gip = True
    while gip == True:
        Hmove = int(input("where would you like to place your token?(1, 2, 3...)"))
        Hmove -= 1
        print_symbol(HUMAN, Hmove)

        print_board()


    # check column not full
    # check for win or no more spaces left
    # make computer move
    # check for win or no more spaces left

    # Win end : congratulate winner
    # offer rematch






