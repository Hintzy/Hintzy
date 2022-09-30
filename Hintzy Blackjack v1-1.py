# Hintzy Blackjack
# v1.0 - initial functional program
# v1.1 - renamed variables and cleaned up comments for readability

import random
import time

# define global variables & lists
deck = []
p_hand = []
h_hand = []
deck_indices = []
p_faces = []
p_suits = []
p_values = []
h_faces = []
h_suits = []
h_values = []
p_sum = 0
h_sum = 0
player_stack = int(1000)
bet = 0
outcome = str()


def build_deck():
    # creates the deck by iterating through all suits and face values for cards creating a list of 52 tuples
    # card list values: 1st = card index, 2nd = card face value, 3rd = card suit, 4th = integer value of card
    # (function ace_fix handles conditional value formatting of aces)
    suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
    face_val = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    card_val = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card_index = 0
    # iterate through all face value and suit combinations, adding an overall card index and integer face value for the
    # card at each iteration
    for x in suit:
        for y in face_val:
            cvind = face_val.index(y)
            current_card = [card_index, y, x, card_val[cvind]]
            global deck
            deck.append(current_card)
            card_index += 1


def deal_hand():
    # deal hands by random sampling of cards from the deck list and use the to be determined "remove_cards" functions
    # them from the deck list inventory
    global p_hand, h_hand, p_sum, h_sum
    p_hand = random.sample(deck, k=2)
    remove_cards(p_hand)
    h_hand = random.sample(deck, k=2)
    remove_cards(h_hand)
    p_stat_reset()
    h_stats_reset()
    calc_hand_value()


def calc_hand_value():
    # calculates the numerical summation of both player and house hands
    global p_sum, h_sum
    p_sum = 0
    h_sum = 0
    y = 0
    z = 0
    while y < len(p_hand):
        p_sum = p_sum + p_values[y]
        y += 1
    while z < len(h_hand):
        h_sum = h_sum + h_values[z]
        z += 1


def deal_player_card():
    # deal a single card to the player by random sampling of one card from the deck and using "removecard" function
    global p_hand
    new_card = random.sample(deck, k=1)
    p_hand = p_hand + new_card              # add randomly selected card to the p_hand list
    remove_cards(p_hand)                    # remove the new card from the deck
    p_stat_reset()                          # redefine the stat lists for player hand to include new card values
    calc_hand_value()                       # recalculate hand value with new card (redundant house hand calculation)


def deal_house_card():
    # deal a card to the house by random sampling of one card from the deck
    global h_hand
    new_card = random.sample(deck, k=1)
    h_hand = h_hand + new_card
    remove_cards(h_hand)
    h_stats_reset()
    calc_hand_value()


def p_stat_reset():
    # repopulate the reference value lists for the player hand with the current full hand
    global p_faces, p_suits, p_values
    p_faces.clear()
    p_suits.clear()
    p_values.clear()
    p_faces = [x[1] for x in p_hand]
    p_suits = [x[2] for x in p_hand]
    p_values = [x[3] for x in p_hand]


def h_stats_reset():
    # repopulate the reference value lists for the house hand with the current full hand
    global h_faces, h_suits, h_values
    h_faces.clear()
    h_suits.clear()
    h_values.clear()
    h_faces = [x[1] for x in h_hand]
    h_suits = [x[2] for x in h_hand]
    h_values = [x[3] for x in h_hand]


def remove_cards(hand):
    # find cards in the main deck that share the indices of the cards with the specified hand and removes them from
    # the deck
    for y in [x[0] for x in hand]:                   # get card indeces of the two cards that were dealt
        global deck_indices
        deck_indices = [x[0] for x in deck]          # for a list of the card indeces in the current deck
        if y in deck_indices:                        # compare card indeces of player hand to card indeces of the deck
            deck.pop(deck_indices.index(y))          # remove the card from the deck that matches the deck indices


def print_p_hand():
    print("\nPlayer's hand:")
    global p_sum
    y = 0
    while y < len(p_hand):
        print(f"{p_faces[y]} of {p_suits[y]}")
        y += 1
    print("Player hand value:", p_sum)


def print_h_hand():
    print("\nThe house shows:")
    print(f"{h_faces[0]} of {h_suits[0]}\n")


def black_jack_check():
    # checks the player and house hands for natural blackjacks
    global outcome
    if p_sum == 21:
        print("A natural blackjack! Checking the house's hand for natural blackjack...")
        if h_sum == 21:
            outcome = "push"
            print("The house also had a natural blackjack! It's a push!")
            stack_adjust()
        else:
            print("The house's hand is not a natural blackjack. Player wins 1.5x of their bet.\n")
            outcome = "blackjack"
            stack_adjust()
    else:  # if players hand isn't a blackjack then still check for a house blackjack
        black_jack_faces = ["Ten", "Jack", "Queen", "King", "Ace"]
        if h_faces[0] in black_jack_faces:
            print("Checking house hole card for a natural blackjack...", end=" ")
            time.sleep(1)
            if h_sum == 21:
                print(f"It's the {h_faces[1]} of {h_suits[1]}!")
                print("The house hit a natural blackjack! Better luck next hand!\n")
                outcome = "lose"
                stack_adjust()
            else:
                print("The house's hand is not a natural blackjack.\n")
                player_choice()
        else:
            player_choice()


def player_choice():
    global p_hand, p_sum, outcome
    print("How would you like to proceed?")
    election = input("Hit = H, Stand = S : ")
    if election == "H":
        deal_player_card()
        if p_sum < 21:
            print_p_hand()
            print_h_hand()
            player_choice()
        if p_sum == 21:
            print_p_hand()
            print("You hit 21. Dealing out the house hand...\n")
            deal_out_house()
        if p_sum > 21:
            if "Ace" in [x[1] for x in p_hand]:
                if [x[1] for x in p_hand].count("Ace") > [x[3] for x in p_hand].count(1):
                    ace_fix(p_hand)
                    p_stat_reset()
                    calc_hand_value()
                    print_p_hand()
                    print_h_hand()
                    player_choice()
                else:
                    print_p_hand()
                    print(f"\nPlayer Hand = {p_sum}\nHouse Hand = {h_sum}")
                    print("You busted. Better luck next hand!\n")
                    outcome = "lose"
                    stack_adjust()
            else:
                print(f"\nPlayer Hand = {p_sum}\nHouse Hand = {h_sum}")
                print("\nYou busted. Better luck next hand!\n")
                outcome = "lose"
                stack_adjust()
    if election == "S":
        deal_out_house()


def deal_out_house():
    global h_sum, h_hand, h_faces, h_suits, outcome
    print("\nThe house shows:")
    print(f"{h_faces[0]} of {h_suits[0]}")              # shows the two hole cards for the house
    time.sleep(1)
    print(f"{h_faces[1]} of {h_suits[1]}")
    time.sleep(1)
    while h_sum <= 16:                                  # if the hole cards are less than or equal to 16
        deal_house_card()                               # another card is dealt and printed using the index of the
        print(f"{h_faces[-1]} of {h_suits[-1]}")        # last card in the house hand list
        time.sleep(1)
    print("")
    if h_sum > 21:                                      # if the house hand exceeds 21 the hand is checked for aces
        if "Ace" in [x[1] for x in h_hand]:
            if [x[1] for x in p_hand].count("Ace") > [x[3] for x in p_hand].count(1):
                ace_fix(h_hand)
                h_stat_reset()
                calc_hand_value()
                print_h_hand()
                deal_out_house()
            else:
                print(f"\nPlayer Hand = {p_sum}\nHouse Hand = {h_sum}")
                print("The house busted. Player wins the hand!\n")
                outcome = "win"
                stack_adjust()
        else:
            print("Player Hand = {}\nHouse Hand = {}".format(p_sum, h_sum))
            print("\nThe house busts. Player wins the hand!\n")
            outcome = "win"
            stack_adjust()
    else:
        if p_sum > h_sum:
            print("Player Hand = {}\nHouse Hand = {}".format(p_sum, h_sum))
            print("\nThe player wins the hand with a total hand of", p_sum, "\b.\n")
            outcome = "win"
            stack_adjust()
        if p_sum == h_sum:
            print("Player Hand = {}\nHouse Hand = {}".format(p_sum, h_sum))
            print("\nIt's a push! Replay the hand...\n")
            outcome = "push"
            stack_adjust()
        else:
            print("Player Hand = {}\nHouse Hand = {}".format(p_sum, h_sum))
            print("\nThe house wins the hand with a total hand of", h_sum, "\b.\n")
            outcome = "lose"
            stack_adjust()


def ace_fix(hand_name):
    y = 0
    for x in hand_name:
        if x[1] == "Ace":
            x[3] = 1
            y += 1
        else:
            y += 1


def betsize():
    global bet, player_stack
    print("Player's stack size: ${}".format(player_stack))
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


def stack_adjust():
    global player_stack
    if outcome == "win":
        player_stack = player_stack + bet
    if outcome == "blackjack":
        player_stack = int(player_stack + (bet * 1.5))
    if outcome == "lose":
        player_stack = player_stack - bet
    if outcome == "push":
        pass
    if player_stack > 0:
        resetall()
        gameon()
    else:
        print("Game Over. As the saying goes... \"The house always wins\".")


def gameon():
    build_deck()
    betsize()
    deal_hand()
    print_p_hand()
    print_h_hand()
    black_jack_check()


def resetall():
    # reset all variables except for the player stack size
    global deck, p_hand, h_hand, deck_indices, p_faces, p_suits, p_values, h_faces, h_suits, h_values, p_sum, h_sum
    global bet, outcome
    deck = []
    p_hand = []
    h_hand = []
    deck_indices = []
    p_faces = []
    p_suits = []
    p_values = []
    h_faces = []
    h_suits = []
    h_values = []
    p_sum = 0
    h_sum = 0
    bet = 0
    outcome = str()


print("Welcome to Hintzy's Blackjack v1.0.  The game will be played with a single deck.")
print("Split hands cannot be played because my coding isn't there yet.")
print("The player will start with $1000 and bets can be placed in increments of $100.\n")

gameon()

'''
build_deck()
deal_hand()

print("\n\nNon-visible metrics:")
print("Player hand = ", p_hand)
print("Player hand value:",p_sum)
print("House hand = ", h_hand)
print("House hand value:",h_sum)
print("Deck =", deck)
'''