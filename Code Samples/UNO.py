from random import shuffle, choice
from time import sleep

class Card:
    def __init__(self, color, number, kind): #kind is used because type is reserved
        self.color = color #Red, Blue, Green, Yellow, None
        self.number = number # 0-9, None
        self.kind = kind #Normal, Skip, Reverse, Draw Two, Wild, Wild Draw Four

    def display(self): #returns a string of what card it is, e.g. Blue 1, or Green Wild
        if self.number != None:
            return self.color + " " + str(self.number)
        elif self.color:
            return self.color + " " + self.kind
        else:
            return self.kind


class Deck:
    def __init__(self):
        self.deck = []
        self.discard = []
        for color in ["Red", "Blue", "Green", "Yellow"]:
            for i in range(10):
                self.deck.append(Card(color, i, "Normal"))
            for i in range(1,10):
                self.deck.append(Card(color, i, "Normal"))
            for kind in ["Skip", "Reverse", "Draw Two"]:
                self.deck.append(Card(color, None, kind))
                self.deck.append(Card(color, None, kind))
        for kind in ["Wild", "Wild Draw Four"]:
            for _ in range(4):
                self.deck.append(Card(None, None, kind))
        shuffle(self.deck)
        self.curr = None #Top of the discard pile

    def draw(self): #gives the player a card, reshuffles the discard pile if there are no cards left
        if len(self.deck) == 0:
            self.deck = self.discard
            shuffle(self.deck)
            self.discard = []
        return self.deck.pop()

    def play(self, card): #*cards? to be considered
        if card == "Win": #Handle win condition
            return card
		#Only special cards, cards that match color, or normal cards of the same number are accepted
        elif card.kind == "Wild" or card.kind == "Wild Draw Four" or card.color == self.curr.color or (card.number == self.curr.number and card.kind == "Normal"):
            if self.curr.kind == "Wild" or self.curr.kind == "Wild Draw Four":
                self.curr.color = None
            self.discard.append(self.curr) #move top card to discard pile
            self.curr = card #Make card played the top card
            return card.kind #If there are any actions to take, pass back to controller
        else:
            return False  #This only triggers if there is an error


class Player:
    def __init__(self, no, hand): #cannot be changed
        self.no = no 
        self.hand = hand 

    def draw(self): #Default function, draws a card from the deck
        card = deck.draw()
        self.hand.append(card)
        return card

    def check_playable(self, card): #Checks if a card can be played, so that it won't be rejected by deck
        if card.color == deck.curr.color or card.color == None or (card.number == deck.curr.number and card.kind == "Normal"):
            return True

    def get_no(self): #Returns player number
        return str(self.no)
    
    def play(self): #This function should be rewritten to be smarter
        print("Hand", str([card.display() for card in self.hand])) #Transparency, shows the hand to viewers
        for card in self.hand: 
            if self.check_playable(card):
                self.hand.remove(card)
                if not card.color: #Choose a random color if card being played is a wildcard
                    card.color = choice(["Red", "Blue", "Green", "Yellow"])
                if len(self.hand) == 1:
                    print("UNO!")
                elif len(self.hand) == 0:
                    return "Win"
                return card
        while not self.check_playable(card): #No cards to play, so have to draw cards
            card = self.draw()
            print("Drew", card.display())
        self.hand.remove(card)
        if not card.color:
            card.color = choice(["Red", "Blue", "Green", "Yellow"])
        if len(self.hand) == 1:
            print("UNO!")
        return card

#more functions can be added to this class
    
#Function to move turn to next player
def increment(turn, players):
    if turn == players - 1:
        return 0
    else:
        return turn + 1  

#Initialize Variables
deck = Deck()
players = [Player(i+1,[deck.draw()for _ in range(7)]) for i in range(4)] #Four identical players, can be changed
won = False
turn = -1
action = True

#Distribute Cards, and flip the first card, taking actions where necessary
while not deck.curr:
    card = deck.draw()
    if card.color != None:
        deck.curr = card
    else:
        deck.deck.insert(0, card)
if deck.curr.kind == "Draw Two":
    for _ in range(2):
        players[0].draw()
    turn = 0
elif deck.curr.kind == "Skip":
    turn = 0
elif deck.curr.kind == "Reverse":
    turn = 0
    players = [players[turn]] + players[:turn][::-1] + players[turn+1:][::-1]
    
print("Cards distributed!")
print("First card is", deck.curr.display())

#Main Loop
while not won:
    turn = increment(turn, len(players)) #Move to next player
    print("Player " + players[turn].get_no() + "'s turn!") 
    action = deck.play(players[turn].play()) #This is the most important code, it asks player to play a card, passes to deck, and stores any actions
    print("Player " + players[turn].get_no() + " played", deck.curr.display())
    if action == "Skip":
        turn = increment(turn, len(players))
    elif action == "Reverse":
        players = [players[turn]] + players[:turn][::-1] + players[turn+1:][::-1]
        turn = 0
    elif action == "Draw Two":
        for _ in range(2):
            players[increment(turn, len(players))].draw()
        turn = increment(turn, len(players))
    elif action == "Wild Draw Four":
        for _ in range(4):
            players[increment(turn, len(players))].draw()
        turn = increment(turn, len(players))
    elif action == "Win":
        print("Player " + players[turn].get_no() + " wins!")
        break
    elif action == False:
        print("Error")
        break    
