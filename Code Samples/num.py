from random import randint
from time import sleep
MAX = 5

class Number:
    def __init__(self, index, num, x, y, direction):
        self.index = index
        self.num = num
        self.x = x
        self.y = y
        self.dir = direction

    def move(self, numbers):
        if (self.x == MAX-1 and self.dir[0] == 1) or (self.x == 0 and self.dir[0] == -1):
            if self.num > 1:
                self.dir = [self.dir[0]*-1,0]
                self.num //= 2
                numbers.append(Number(len(numbers),self.num,self.x,self.y,[0,[-1,1][randint(0,1)]]))
            else:
                self.num = "-"
                self.dir = [0,0]
        elif (self.y == 0 and self.dir[1] == -1) or (self.y == MAX-1 and self.dir[1] == 1):
            if self.num > 1:
                self.dir = [0,self.dir[1]*-1]
                self.num //= 2
                numbers.append(Number(len(numbers),self.num,self.x,self.y,[[-1,1][randint(0,1)],0]))
            else:
                self.num = "-"
                self.dir = [0,0]
        self.x += self.dir[0]
        self.y += self.dir[1]
        return numbers
    
    def display(self, board, numbers):
        if board[self.x][self.y] != "-":
            other = numbers[board[self.x][self.y]]
            if other.num == "-":
                board[self.x][self.y] = self.index
            elif self.num == "-":
                pass
            elif other.num == self.num:
                other.num = "-"
                other.dir = [0,0]
                self.num *= 2
                board[self.x][self.y] = self.index
            elif other.num < self.num:
                self.num = self.num + other.num-other.num%2
                other.num = "-"
                other.dir = [0,0]
                board[self.x][self.y] = self.index
            else:
                other.num = other.num + self.num-self.num%2
                self.num = "-"
                self.dir = [0,0]
                board[self.x][self.y] = other.index
        else:
            board[self.x][self.y] = self.index
        return board, numbers

numbers = [Number(x, 4,randint(0,4),randint(0,4),[[0,1],[0,-1],[-1,0],[1,0]][randint(0,3)]) for x in range(randint(3,5))]  
while True:
    board = [["-"]*MAX for _ in range(MAX)]    
    for number in numbers:
        numbers = number.move(numbers)
        board, numbers = number.display(board, numbers)
    print("\n"*100)
    if board == [["-"]*MAX for _ in range(MAX)]:
        numbers = [Number(x, 4,randint(0,4),randint(0,4),[[0,1],[0,-1],[-1,0],[1,0]][randint(0,3)]) for x in range(randint(3,5))]  
    for row in board:
        for item in row:
            if item == "-":
                print(item, end=" ")
            else:
                print(numbers[item].num, end=" ")
        print("")
    sleep(1)
