from random import randint
from random import shuffle

#Initialize an empty board
#Create a constant for the board size, the board should be 10 by 10

#Build board as a nested array of ten "O"s by ten "O"s

    

randomrow = [0,1,2,3,4,5,6,7,8,9]
shuffle(randomrow)
#Create an array of ships with the format ["Name",Col,Row,Number of pieces, number of pieces] the first has been done, make four more.
ships=[["carrier",randint(0,5),randomrow[0],5,5]]

#Print each row of board on a new line


#Define two functions get_row to obtain a row and get_col to obtain a column from the player



def check_input(row,col):
    try:
        row = int(row)-1
        col = int(col)-1
        #Check input to see if the user entered a coordinate not on the board or a point which has already been revealed, return False if this is the case.
        return True
    except ValueError:
        return False

    
#Try to understand how the check hit function works 
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
        print("You missed.")
        board[row][col] = "@"

#Define a function check_win to check for a win by iterating through the ships and checking if ship[3]==0 for each of them, returning True of all ships have been sunk.



print("Let's play Battleship!")
print("You have 30 turns to sink all the ships. \nSelect a row and column between 1 and 10 as a target. \nO denotes an unknown spot. @ denotes an empty spot. \nX denotes a hit. - denotes a sunken ship.")
#Print the board
for turn in range(100):
    #Get the column and row, storing the result to the variables col and row
    #Check the validity of the input and ask the user to try again if input is invalid
    row = int(row)-1
    col = int(col)-1
    check_hit(row,col)
    #If the user has won, print "You win" and exit loop
    #Print the board again
    #If the player has exceeded to maximum amount of turns, exit the loop and print "Game over"
    #Tell the player what turn it is
    #You can use a print(ships) statement to debug, don't forget to remove it or comment it out so that the actual players can't cheat! 
