#Import from library
from random import randint
from random import shuffle

#Initialize board
board = #(an empty array)
board_size = 10

#Build board
for x in range(board_size):
    board.#(function to add to end of array)(["O"] * board_size)
    
#Place ships
randomrow = [0,1,2,3,4,5,6,7,8,9]
shuffle(randomrow)
ships=[["carrier",randint(0,5),randomrow[0],5,5],["battleship",randint(0,6),randomrow[1],4,4],["cruiser",randint(0,7),randomrow[2],3,3],["submarine",randint(0,8),randomrow[3],2,2],["destroyer",randint(0,8),randomrow[4],2,2]]

#Print board
def print_board():
    #(loop through each row in the board)
        print(" ".join(row))

#Get input
def get_row():
    return input("Guess Row:")
#(define a similar function to get the Col)
    #(function returns the user input)

#Check input
def check_input(row,col):
    try:
        row = int(row)-1
        col = int(col)-1
        if (row < 0 or row > board_size) or #(check if the Col is out of range):
            print("Oops, that's not even in the ocean.")
            return False
        elif board[row][col] == "@" or board[row][col] == "X" or board[row][col] == "-":
            print(#(What should the player see in this case?))
            return False
        return True
    except ValueError:
        return False

    
#Check for hit
def check_hit(row,col):
    hit = 0
    for ship in ships:
        if ship[1] <= col <= (ship[1]+ship[4]) and row == ship[2]:
            hit = 1
            ship[3] -= 1
            if ship[3] == 0:
                print("You sank the",ship[0],"!")
                for i in range(ship[4]):
                    board[ship[2]][ship[1]+i] = "-"
            else:
                print("You hit a ship!")
                board[row][col] = "X"
    if hit == 0:
        print(#(What should the player see in this case?))
        board[row][col] = "@"

#Check for win
def check_win():
    #(loop through ships)
        #(check if there are any pieces of the ship left)
            return False
    return True

#Main
print("Let's play Battleship!")
print("You have 30 turns to sink all the ships. \nSelect a row and column between 1 and 10 as a target. \nO denotes an unknown spot. @ denotes an empty spot. \nX denotes a hit. - denotes a sunken ship.")
print_board()
for turn in range(100):
    row = get_row()
    col = get_col()
    #(while the input is invalid)
        #(tell the player to try again)
        #(get col again)
        #(get row again)
    row = int(row)-1
    col = int(col)-1
    check_hit(row,col)
    #(if the player has won)
        #(tell the player that they have won)
        #(exit loop)
    print_board()
    #(if the player has exceeded to maximum amount of turns)
        #(tell the player game over)
        #(exit the loop)
    print("Turn",turn+1)
    #(you can use print(ships) here to cheat!)
