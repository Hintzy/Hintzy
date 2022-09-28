deck = []
suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
faceval = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]


for x in range(0,4):
    print('{:<20}'.format(suit[x]), end="")
print("")
for x in faceval:
    print("")
    for y in suit:
        print('{:<6} of {:<10}'.format(x,y), end="")
       