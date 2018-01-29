# Import from library
from random import randint
from random import shuffle

# Initialize board
board = []
board_size = 10

# Build board
for x in range(board_size):
    board.append(["O"] * board_size)

# Place ships
randomrow = [0,1,2,3,4,5,6,7,8,9]
shuffle(randomrow)
ships = [["carrier",randint(0,5),randomrow[0],5,5],["battleship",randint(0,6),randomrow[1],4,4],["cruiser",randint(0,7),randomrow[2],3,3],["submarine",randint(0,8),randomrow[3],2,2],["destroyer",randint(0,8),randomrow[4],2,2]]


# Print board
def print_board():
    for row in board:
        print(" ".join(row))


# Get input
def get_row():
    return input("Guess Row:")
def get_col():
    return input("Guess Col:")


# Check input
def check_input(row, col):
    try:
        row = int(row)-1
        col = int(col)-1
        if (row < 0 or row > board_size) or (col < 0 or col > board_size):
            print("Oops, that's not even in the ocean.")
            return False
        elif board[row][col] == "@" or board[row][col] == "X" or board[row][col] == "-":
            print("You guessed that one already.")
            return False
        return True
    except ValueError:
        return False


# Check for hit
def check_hit(row, col):
    hit = 0
    for ship in ships:
        if ship[1] <= col <= (ship[1]+ship[4]) and row == ship[2]:
            hit = 1
            ship[3] -= 1
            if ship[3] == 0:
                print("You sank the", ship[0], "!")
                for i in range(ship[4]):
                    board[ship[2]][ship[1]+i] = "-"
            else:
                print("You hit a ship!")
                board[row][col] = "X"
    if hit == 0:
        print("You missed.")
        board[row][col] = "@"


# Check for win
def check_win():
    for ship in ships:
        if ship[3] != 0:
            return False
    return True


# Main
print("Let's play Battleship!")
print("You have 30 turns to sink all the ships. \nSelect a row and column between 1 and 10 as a target. \nO denotes an unknown spot. @ denotes an empty spot. \nX denotes a hit. - denotes a sunken ship.")
print_board()
for turn in range(100):
    row = get_row()
    col = get_col()
    while check_input(row, col) is False:
        print("Try again")
        col = get_col()
        row = get_row()
    row = int(row)-1
    col = int(col)-1
    check_hit(row, col)
    if check_win():
        print("You win!")
        break
    print_board()
    if turn == 30:
        print("You lose!")
        break
    print("Turn", turn+1)
#   print(ships)
