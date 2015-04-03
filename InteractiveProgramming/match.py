# implementation of card game - Memory

import simplegui
import random
from math import sqrt

cards = list()       # list to hold the cards
card_size = 50       # x dimension of card (y dimension is calculated based on this)
margins = ( 20, 20 ) # spacing around edges
pad = ( 10, 10 )     # intercard spacing
showtime = 700       # number of milliseconds to show second revealed card
matchtime = 350      # number of milliseconds to show revealed, matched cards

game = {
         'best' : 0,
         'draws' : 0,
         'drawn' : None,
         'match' : None,
       }

w = card_size		 # width of a card is the card_size
h = ((1 + sqrt(5)) / 2 ) *card_size # height of a card is phi times width

for x in range(4):
    for y in range(4):
        xpos = margins[0] + x * ( w + pad[0] ) - 0.5
        ypos = margins[1] + y * ( h + pad[1] ) - 0.5
        # remember: x is horizontal offset, y is vertical offset
        cards.append( { 'location' : { 'x' : xpos, 'y' : ypos },
                        'value' : 'A',
                        'size' : { 'x' : w, 'y' : h },
                        'face' : False,
                        'color' : 'red',
                        'fill' : 'green',
                        'fontcolor' : 'yellow',
                        'fontsize' : 30,
                        'linewidth' : 2,
                        'drawn' : True,
                       })

def initialize_cards():
    global cards
    card_values = range(8) + range(8)
    random.shuffle(card_values)
    for i in range(len(card_values)):
        cards[i]['value'] = card_values[i]
        cards[i]['face'] = False
        cards[i]['drawn'] = True
        
def draw_card( card, canvas ):
    
    if not card['drawn']: return

    x = card['location']['x']
    y = card['location']['y']
    w = card['size']['x']    
    h = card['size']['y']
    
    loc = [
              ( x, y ),
              ( x, y+h ),
              ( x+w, y+h ),
              ( x+w, y),
          ] 
    
    canvas.draw_polygon(loc, card['linewidth'], card['color'], card['fill'])
    if card['face']:
        tx = x + w/2 - card['fontsize']/4
        ty = y + h/2 + card['fontsize']/4
        canvas.draw_text(str(card['value']), (tx,ty), card['fontsize'], card['fontcolor'])

def hide_all():
    for card in cards:
        card['face'] = False
    if showtimer.is_running(): showtimer.stop()
        
def show_all():
    for card in cards:
        card['face'] = True
    if showtimer.is_running(): showtimer.stop()

def hide_matches():
    game['drawn']['drawn'] = False
    game['drawn'] = False
    game['match']['drawn'] = False
    game['match'] = False
    if matchtimer.is_running(): matchtimer.stop()
    any = False
    for card in cards:
        any = any or card['drawn']
    if not any:
        if game['draws'] < game['best'] or game['best'] == 0: game['best'] = game['draws']
        animationtimer.start()
        
# helper function to initialize globals
def new_game():
    initialize_cards()
    game['draws'] = 0
    game['drawn'] = False
    game['match'] = False
    if animationtimer.is_running(): animationtimer.stop()
    if showtimer.is_running(): showtimer.stop()
    if matchtimer.is_running(): matchtimer.stop()

def clicked(card,pos):
    if not card['drawn'] or card['face']: return False
    x = card['location']['x']
    y = card['location']['y']
    w = card['size']['x']    
    h = card['size']['y']

    return not ( pos[0] < x or pos[0] > x + w or pos[1] < y or pos[1] > y + h )
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, hidetimer, showtimer
    if showtimer.is_running() or matchtimer.is_running(): return
    for card in cards:
        if clicked(card,pos):
            card['face'] = True
            if not game['drawn']:
                game['drawn'] = card
            elif card['value'] == game['drawn']['value']:
                game['match'] = card
                game['draws'] += 1
                matchtimer.start()
            else:
                game['drawn'] = None
                game['draws'] += 1
                showtimer.start()
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in cards:
        draw_card(card,canvas)
    label.set_text("Turns = " + str(game['draws']))
    if game['best'] > 0:
        best.set_text("Best = " + str(game['best'])) 

def animate():
    pass
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", margins[0] + 4 * (w + pad[0]) + margins[0]/2,
                                         margins[1] + 4 * (h + pad[1]) + margins[1]/2)
line = frame.add_label("----------------------------")
label = frame.add_label("Turns = 0")
best = frame.add_label("Best = 0")
line = frame.add_label("----------------------------")
frame.add_button("New Game", new_game)
line = frame.add_label("----------------------------")
#line = frame.add_label("----------DEBUGGING---------")
#frame.add_button("Show All", show_all)
#frame.add_button("Hide All", hide_all)


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

showtimer = simplegui.create_timer(showtime,hide_all)
matchtimer = simplegui.create_timer(matchtime,hide_matches)
animationtimer = simplegui.create_timer(1,animate)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric