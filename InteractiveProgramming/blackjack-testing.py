# Mini-project #6 - Blackjack

#import simplegui
import random

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
#card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
#card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize global variables
deck = []
player_hand = None
dealer_hand = None
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.face = True
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self,canvas,pos):
        if self.face: 
            self.draw_front(canvas,pos)
        else:
            self.draw_back(canvas,pos)
            
    def draw_front(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_SIZE[0] / 2, pos[1] + CARD_SIZE[1] / 2], CARD_SIZE)
        
    def draw_back(self,canvas,pos):    
        canvas.draw_image(card_back, (CARD_BACK_SIZE[0] * 0.5, CARD_BACK_SIZE[1] * 0.5), CARD_BACK_SIZE, [pos[0] + CARD_BACK_SIZE[0] / 2, pos[1] + CARD_BACK_SIZE[1] / 2], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return " ".join([str(card) for card in self.cards]) + " Total: " + self.get_value()

    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if don't bust
    def get_value(self):
        sum = sum([VALUE[card.get_rank()] for card in self.cards])
        if sum < 12 and filter(card.rank == 'A', self.cards):
            sum += 10
        return sum
    
    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, p):
        pos = [p[0],p[1]] # make a copy as a list so we can modify it
        cardno = 0
        for card in self.cards:
            pos[0] = cardno * CARD_SIZE[0]
            card.draw(canvas,pos)
            cardno += 1
 
        
# define deck class
class Deck:
    def __init__(self):
        self.cards = []

    # add cards back to deck and shuffle
    def shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


#define callbacks for buttons
def deal():
    global outcome, in_play, deck
    deck.shuffle()
    outcome = ""
    in_play = True

def hit():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play:
        player_hand.add_card(deck.deal_card())
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
    if player_hand.busted():
        outcome = "Busted!!!"
        in_play = False
        score -= 1
       
def stand():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
   
    if dealer_hand.busted() or dealer_hand.get_value() < player_hand.get_value():
        outcome = "Win!!!"
        in_play = False
        score += 1
    else:
        outcome = "Lose..."
        in_play = False
        score -= 1
    # assign a message to outcome, update in_play and score

def draw(canvas):
    canvas.draw_text("BlackJack! (Dealer hits on 16- and stays on 17+)",(0,25),25,"Yellow")
    canvas.draw_text("Dealer",(20,100),20,"Yellow")
    dealer_hand.draw(canvas,(20,103))
    canvas.draw_text("Player",(20,250),20,"Yellow")
    player_hand.draw(canvas,(20,253))
    canvas.draw_text("Score = %s"%(score), (200,200),25,"Red")
    canvas.draw_text(outcome,(200,220),25,"Blue")


# initialization frame
#frame = simplegui.create_frame("Blackjack", 600, 400)
#frame.set_canvas_background("Green")

#create buttons and canvas callback
#frame.add_button("Deal", deal, 200)
#frame.add_button("Hit",  hit, 200)
#frame.add_button("Stand", stand, 200)
#frame.set_draw_handler(draw)

# deal an initial hand
dealer_hand = Hand()
player_hand = Hand()
deck = Deck()
deck.shuffle()

dealer_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())

# get things rolling
#frame.start()

print dealer_hand
print player_hand
# Grading rubric - 18 pts total (scaled to 100)

# 1 pt - The program opens a frame with the title "Blackjack" appearing on the canvas.
# 3 pts - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area. (1 pt per button)
# 2 pts - The program graphically displays the player's hand using card sprites. 
#		(1 pt if text is displayed in the console instead) 
# 2 pts - The program graphically displays the dealer's hand using card sprites. 
#		Displaying both of the dealer's cards face up is allowable when evaluating this bullet. 
#		(1 pt if text displayed in the console instead)
# 1 pt - Hitting the "Deal" button deals out new hands to the player and dealer.
# 1 pt - Hitting the "Hit" button deals another card to the player. 
# 1 pt - Hitting the "Stand" button deals cards to the dealer as necessary.
# 1 pt - The program correctly recognizes the player busting. 
# 1 pt - The program correctly recognizes the dealer busting. 
# 1 pt - The program correctly computes hand values and declares a winner. 
#		Evalute based on player/dealer winner messages. 
# 1 pt - The dealer's hole card is hidden until the hand is over when it is then displayed.
# 2 pts - The program accurately prompts the player for an action with the messages 
#        "Hit or stand?" and "New deal?". (1 pt per message)
# 1 pt - The program keeps score correctly.
