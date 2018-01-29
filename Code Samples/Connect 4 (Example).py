# Connect 4

# Initialize variables and constants
leave = False
board = []
board_width = 7
board_height = 6
turn = 1
token = ["|O|", "|X|"]

# Build board
for i in range(board_height):
    row = []
    for j in range(board_width):
        row.append("|_|")
    board.append(row)


# Print board
def print_board():
    for row in board:
        print(" ".join(row))


# Check if column is full
def test_insert(column, turn):
    for i in range(board_height-1, -1, -1):
        if board[i][column-1] == "|_|":
            return True
    return False


# Insert token
def insert(column, turn):
    for i in range(board_height-1, -1, -1):
        if board[i][column-1] == "|_|":
            board[i][column-1] = token[turn-1]
            break


# Test if board exists
def board_exist(height, row):
    if board_height > height >= 0:
        if board_width > row >= 0:
            return True
    return False


# Test for win
def win_test(turn):
    wincon = 0
    for i in range(board_height):
        wincon = 0
        for j in range(board_width):
            if board[i][j] == token[turn-1]:
                wincon += 1
            if wincon == 4:
                return True
            else:
                wincon = 0

    for i in range(board_width):
        wincon = 0
        for j in range(board_height):
            if board[j][i] == token[turn-1]:
                wincon += 1
            else:
                wincon = 0
            if wincon == 4:
                return True

    # diagonal test (up-left to down-right)
    for j in range(board_width):
        wincon = 0
        for d in range(board_width):
            if board_exist(d, j+d):
                if board[d][j+d] == token[turn-1]:
                    wincon += 1
                else:
                    wincon = 0
                if wincon == 4:
                    return True

    for j in range(board_height):
        wincon = 0
        for d in range(board_height):
            if board_exist(j+d, d):
                if board[j+d][d] == token[turn-1]:
                    wincon += 1
                else:
                    wincon = 0
                if wincon == 4:
                    return True

    # diagonal test cont (down-left to up-right)
    for j in range(board_width):
        wincon = 0
        for d in range(board_width):
            if board_exist(board_width-1-d, j+d):
                if board[board_width-1-d][j+d] == token[turn-1]:
                    wincon += 1
                else:
                    wincon = 0
                if wincon == 4:
                    return True
        

    for j in range(board_height-1, -1, -1):
        wincon = 0
        for d in range(board_height):
            if board_exist(j-d, d):
                if board[j-d][d] == token[turn-1]:
                    wincon += 1
                else:
                    wincon = 0
                if wincon == 4:
                    return True


# Test if board is full
def board_full_test():
    for i in range(board_height):
        for j in range(board_width):
            if board[i][j] == "|_|":
                return False
    return True


# Check if input is valid
def validinput(a):
    try:
        a = int(a)
        if 0 < a <= board_width:
            return True
        return False
    except ValueError:
        return False


# Main
print_board()
while not leave:
    input_accepted = False
    while not input_accepted:
        column = input("Player " + str(turn) + " make a choice:")
        if column.lower() == "quit":
            leave = True
            break
        elif validinput(column):
            if test_insert(int(column), turn):
                insert(int(column), turn)
                input_accepted = True
        else:
            print("Error, please try again")
    if leave:
        break
    print_board()
    if win_test(turn):
        print("Player", turn, "wins!")
        break
    elif board_full_test():
        print("Board full, Draw.")
        break
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

