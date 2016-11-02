import random

playing = False
chip_pool = 100
bet = 1
restart_phrase = "Press 'd' to deal teh cards again, or press 'q' to quit"

suits = ('H','D','C','S')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print self.suit + self.rank

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str++()
            hand_comp += "" + card_name
        return 'The hand has %s' %hand_comp

    def card_add(self,card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if(self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self,hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()

class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += "" + deck_comp.__str__()

        return "The deck has " + deck_comp

def make_bet():
    global bet
    bet = 0

    print "What amount of chips would you like to bet? (Enter an integer)"

    while bet == 0:
        bet_comp = raw_input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print "Invalid bet, you only have %s remaining" % chip_pool

def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()

    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Press either h or s: "

    if playing == True:
        print 'Fold, Sorry'
        chip_pool -= bet

    playing = True
    game_step()

def hit():
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet

    if playing:
        if player.hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

        print "player hand is %s" %player_hand

        if player_hand.calc_val() > 21:
            result = "Busted! " + restart_phrase

            chip_pool -= bet
            playing = False
    else:
        result = "Sorry, can't hit " + restart_phrase
    game_step()

def stand():
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet
    ''' This function will now play the dealers hand, since stand was chosen '''

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"

    # Now go through all the other possible options
    else:

        # Soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        # Dealer Busts
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!' + restart_phrase
            chip_pool += bet
            playing = False

        #Player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer, you win!' + restart_phrase
            chip_pool += bet
            playing = False

        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up, push!' + restart_phrase
            playing = False

        # Dealer beats player
        else:
            result = 'Dealer Wins!' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()

def game_step():
    'Function to print game step/status on output'

    #Display Player Hand
    print ""
    print('Player Hand is: '),
    player_hand.draw(hidden =False)

    print 'Player hand total is: '+str(player_hand.calc_val())

    #Display Dealer Hand
    print('Dealer Hand is: '),
    dealer_hand.draw(hidden=True)

    # If game round is over
    if playing == False:
        print  " --- for a total of " + str(dealer_hand.calc_val() )
        print "Chip Total: " + str(chip_pool)
    # Otherwise, don't know the second card yet
    else:
        print " with another card hidden upside down"

    # Print result of hit or stand.
    print result

    player_input()

def game_exit():
    print 'Thanks for playing!'
    exit()

def player_input():
    ''' Read user input, lower case it just to be safe'''
    plin = raw_input().lower()


    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print "Invalid Input...Enter h, s, d, or q: "
        player_input()

def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print statement

'''The following code will initiate the game! (Note: Need to Run all Cells)'''

# Create a Deck
deck = Deck()
#Shuffle it
deck.shuffle()
# Create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()
#Print the intro
intro()
# Deal out the cards and start the game!
deal_cards()
