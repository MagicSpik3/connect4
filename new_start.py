# Define the game board dimensions
my_COLS = 7
my_ROWS = 6

# Define the players
P1 = "X"
P2 = "O"
symbol_list=[P1, P2]

def print_board(board):
    print("-------------")

    num_rows = len(board)
    num_cols = len(board[0])
    print('num_rows', num_rows)
    print('num_cols', num_cols)


    for the_r in range(num_rows):
        #print("the r is:", the_r)
        row = "| "
        for the_c in range(num_cols):
            #print("the c is :", the_c)
            row += board[the_r][the_c] + " | "
        print(row)
        print("-----------------------------")


# prints a board
board = []
for the_r in range(my_ROWS):
    row = []
    for the_c in range(my_COLS):
        #row.append(str(the_r) + str(the_c))
        row.append(' ')
    board.append(row)

#print(matrix)


def print_symbol(symbol, column):
    print(board[0])
    for the_r in range(my_ROWS-1, -1, -1):
        print('r', the_r)
        if board[the_r][column] == " ":
            board[the_r][column] = symbol
            #print("debug")
            break

def get_input(player_turn):
    # Get the user's input for the Column

    message_out = ("Player ", player_turn + 1, ", where would you like to place your token?(1, 2, 3...)")
    while True:
        try:
            Hmove = int(input(message_out))
            if (Hmove < 1) or (Hmove > my_COLS) or (board[0][Hmove-1] != ' '):
                raise ValueError
            return Hmove
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

print_board(board)
player_turn = int(0)
gip = True
while gip == True:

    #print(message_out)
    Hmove = get_input(player_turn)

    Hmove -= 1
    print_symbol(symbol_list[player_turn], Hmove)
    print_board(board)
    # win check
    if (player_turn == 0):
        player_turn = 1
    else:
        player_turn = 0