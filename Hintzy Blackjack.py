#define global variables/lists
deck = []
playerhand = []
househand = []
deckindeces = []
phandfaces = []
phandsuits = []
phandvals = []
hhandfaces = []
hhandsuits = []
hhandvals = []
phandsum = 0
hhandsum = 0
playerstack = int(1000)
bet = 0
outcome = str()

import random
import time

#creates the deck by iterating through all suits and face values for cards creating a list of 52 tuples
#card list values: 1st = card index, 2nd = card face value, 3rd = card suit, 4th = integer value of card (aces to be handled conditionally)
def builddeck():
    suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
    faceval = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    cardval = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cardindex = 0
    #iterate through all face value and suit combinations and add an overall card index and integer value for the card at each iteration
    for x in suit:
        for y in faceval:
            cvind = faceval.index(y)
            currentcard = [cardindex, y, x, cardval[cvind]]
            #global deck
            deck.append(currentcard)
            cardindex += 1
            
#deal hands by random sampling of cards from the current deck and removing them from the deck list inventory
def dealhands():
    global playerhand, househand, phandsum, hhandsum
    playerhand = random.sample(deck,k=2) #pick two cards from the current deck
    removecards(playerhand)
    househand = random.sample(deck,k=2) #pick two cards from the current deck
    removecards(househand)
    playerhandstatsreset()
    househandstatsreset()
    calchandvalues()

def calchandvalues():
    global phandsum, hhandsum
    phandsum = 0
    hhandsum = 0
    y = 0
    while y < len(playerhand):
        phandsum = phandsum + phandvals[y]
        y += 1
    z = 0
    while z < len(househand):
        hhandsum = hhandsum + hhandvals[z]
        z += 1
        
#deal a card to player by random sampling of one card from the deck    
def dealplayercard():
    global playerhand
    newcard = random.sample(deck, k=1)
    playerhand = playerhand + newcard #add randomly selected card to the playerhand list
    removecards(playerhand)  #remove it from the deck
    playerhandstatsreset()
    calchandvalues()

#reset the reference lists for the player hand and reassign values with the new full hand
def playerhandstatsreset(): 
    global phandfaces, phandsuits, phandvals
    phandfaces.clear()  
    phandsuits.clear()
    phandvals.clear()
    phandfaces = [x[1] for x in playerhand]
    phandsuits = [x[2] for x in playerhand]
    phandvals = [x[3] for x in playerhand]

#deal a card to the house by random sampling of one card from the deck    
def dealhousecard():
    global househand
    newcard = random.sample(deck, k=1)
    househand = househand + newcard
    removecards(househand)
    househandstatsreset()
    calchandvalues()

def househandstatsreset():
    global hhandfaces, hhandsuits, hhandvals
    hhandfaces.clear()
    hhandsuits.clear()
    hhandvals.clear()
    hhandfaces = [x[1] for x in househand]
    hhandsuits = [x[2] for x in househand]
    hhandvals = [x[3] for x in househand]
    
#defines a function to find cards in the main deck that share the indeces of the cards in the players hand and remove them
def removecards(z):
    for y in [x[0] for x in z]: #get card indeces of the two cards that were dealt
        global deckindeces
        deckindeces = [x[0] for x in deck] #for a list of the card indeces in the current deck
        if y in deckindeces: #compare card indeces of player hand to card indeces of the deck 
            deck.pop(deckindeces.index(y)) #remove the card from the deck when matching the indeces of the deck

def printplayerhand():
    print("\nPlayer's hand:")
    global phandsum
    y = 0
    while y < len(playerhand):
        phandcard = "{} of {}"
        print(phandcard.format(phandfaces[y],phandsuits[y]))
        y += 1
    print("Player hand value:", phandsum)
    
def printhousehand():
    print("\nThe house shows:")
    hhandcard = "{} of {}\n"
    print(hhandcard.format(hhandfaces[0],hhandsuits[0]))    

def blackjackcheck(): #check the dealt hands for blackjacks
    #if player hits a natural blackjack check if dealers hand is also a blackjack
    global playerstack, outcome
    if phandsum == 21:
        print("A natural blackjack! Checking the house's hand for natural blackjack...")
        if hhandsum == 21:
            outcome = "push"
            print("The house also had a natural blackjack! It's a push!")
            stackadjust()
        else:
            print("The house's hand is not a natural blackjack. Player wins 1.5x of their bet.\n")
            outcome = "blackjack"
            stackadjust()
            
    else: #if players hand isn't a blackjack then still check for a house blackjack
        bjfaces = ["Ten", "Jack", "Queen", "King", "Ace"]
        if hhandfaces[0] in bjfaces: 
            print("Checking house hole card for a natural blackjack...", end=" ")
            time.sleep(1)
            if hhandsum == 21:
                holecard = "It's the {} of {}!"
                print(holecard.format(hhandfaces[1],hhandsuits[1]))
                print("The house hit a natural blackjack! Better luck next hand!\n")
                outcome = "lose"
                stackadjust()
            else:
                print("The house's hand is not a natural blackjack.\n")
                playerchoice()
        else: playerchoice()

def playerchoice():
    global playerhand, phandsum, outcome
    print("How would you like to proceed?")
    election = input("Hit = H, Stand = S : ")
    if election == "H":
        dealplayercard()
        if phandsum < 21:
            printplayerhand()
            printhousehand()
            playerchoice()
        if phandsum == 21:
            printplayerhand()
            print("You hit 21. Dealing out the house hand...")
            dealouthouse()
        if phandsum > 21:
            if "Ace" in [x[1] for x in playerhand]:
                y = 0
                for x in playerhand:
                    if x[1] == "Ace" and x[3] != 1:
                        acefix(playerhand)
                        playerhandstatsreset()
                        calchandvalues()
                        printplayerhand()
                        printhousehand()
                        playerchoice()
                    else:
                        printplayerhand()
                        print("\nPlayer Hand = {}\nHouse Hand = {}".format(phandsum,hhandsum))
                        print("You busted. Better luck next hand!\n")
                        outcome = "lose"
                        stackadjust()
            else:
                printplayerhand()
                print("Player Hand = {}\nHouse Hand = {}\n".format(phandsum,hhandsum))
                print("\nYou busted. Better luck next hand!\n")
                outcome = "lose"
                stackadjust()
    if election == "S":
        dealouthouse()

def dealouthouse():
    global hhandsum, househand, hhandfaces, hhandsuits
    print("\nThe house shows:")
    hhandcard = "{} of {}"
    print(hhandcard.format(hhandfaces[0],hhandsuits[0]))
    time.sleep(1)
    print(hhandcard.format(hhandfaces[1],hhandsuits[1]))
    time.sleep(1)
    housecheck()

def housecheck():
    global outcome
    while hhandsum <= 16:
        dealhousecard()
        hhandcard = "{} of {}"
        print(hhandcard.format(hhandfaces[-1],hhandsuits[-1]))
        time.sleep(1)
    if hhandsum > 21:
        if "Ace" in [x[1] for x in househand]:
            acefix(househand)
            househandstatsreset()
            calchandvalues()
            housecheck()
        else:
            print("Player Hand = {}\nHouse Hand = {}".format(phandsum,hhandsum))
            print("\nThe house busts. Player wins the hand!\n")
            outcome = "win"
            stackadjust()
    else:
        if phandsum > hhandsum:
            print("Player Hand = {}\nHouse Hand = {}".format(phandsum,hhandsum))
            print("\nThe player wins the hand with a total hand of", phandsum,"\b.\n")
            outcome = "win"
            stackadjust()
        if phandsum == hhandsum:
            print("Player Hand = {}\nHouse Hand = {}".format(phandsum,hhandsum))
            print("\nIt's a push! Replay the hand...\n")
            outcome = "push"
            stackadjust()
        else:
            print("Player Hand = {}\nHouse Hand = {}".format(phandsum,hhandsum))
            print("\nThe house wins the hand with a total hand of", hhandsum,"\b.\n")
            outcome = "lose"
            stackadjust()

def acefix(handname):
    y = 0
    for x in handname:
        if x[1] == "Ace":
            x[3] = 1
            y += 1
        else:
            y += 1

def betsize():
    global bet, playerstack
    print("Player's stack size: ${}".format(playerstack))
    bet = input("How much would you like to bet on this hand? ")
    if bet.isdigit():
        if int(bet) % 100 == 0:
            bet = int(bet)
            return bet
        else:
            print("Please enter numeric values only in increments of $100.")
            betsize()
    else:
        print("Please enter numeric values only in increments of $100.")
        betsize()

def stackadjust():
    global playerstack
    if outcome == "win":
        playerstack = playerstack + bet
    if outcome == "blackjack":
        playerstack = playerstack + (bet * 1.5)
    if outcome == "lose":
        playerstack = playerstack - bet
    if outcome == "push":
        pass
    if playerstack != 0:
        resetall()
        gameon()
    else:
        print("Game Over. As the saying goes... \"The house always wins\".")  
    
def gameon():
    builddeck()
    betsize()
    dealhands()
    printplayerhand()
    printhousehand()
    blackjackcheck()

def resetall():
    global deck, playerhand, househand, deckindeces, phandfaces, phandsuits, phandvals, hhandfaces, hhandsuits, hhandvals, phandsum, hhandsum
    deck = []
    playerhand = []
    househand = []
    deckindeces = []
    phandfaces = []
    phandsuits = []
    phandvals = []
    hhandfaces = []
    hhandsuits = []
    hhandvals = []
    phandsum = 0
    hhandsum = 0
    bet = 0
    outcome = str()

print("Welcome to Hintzy's Blackjack v1.0.  The game will be played with a single deck.")
print("Split hands cannot be played because my coding isn't there yet.")
print("The player will start with $1000 and bets can be placed in increments of $100.\n")

gameon()

'''
print("\n\nNon-visible metrics:")
print("Player hand = ", playerhand)
print("Player hand value:",phandsum)
print("House hand = ", househand)
print("House hand value:",hhandsum)
print("Deck =", deck)
'''
