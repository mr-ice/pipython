# implementation of card game - Memory

# I originally coded this with timers for hiding the cards instead of hiding them
# on a mouse click.  And I removed cards that matched instead of leaving them face up.
# I thought it worked pretty well but it didn't meet the requirements of the grading
# rubrick, so I had to make changes.  If you want to see that code, you can see it at
# http://www.codeskulptor.org/#user39_efDZwo8MIu_0.py

import simplegui
import random
from math import sqrt

cards = list()       # list to hold the cards
card_size = 75       # x dimension of card (y dimension is calculated based on this)
margins = ( 20, 20 ) # spacing around edges
pad = ( 10, 10 )     # intercard spacing
##showtime = 700       # number of milliseconds to show revealed, unmatched cards
##matchtime = 350      # number of milliseconds to show revealed, matched cards
fontsize = 35        # size of the font for card faces

game = {
         'over' : False,
         'best' : 0,
         'draws' : 0,
         'drawn' : None,
         'match' : None,
       }
game_over_text = "Game Over!"

animated = False
animation_tick = 0

w = card_size		 # width of a card is the card_size
h = ((1 + sqrt(5)) / 2 ) *card_size # height of a card is phi times width

canvaswidth = margins[0] + 4 * (w + pad[0]) + margins[0]/2
canvasheight = margins[1] + 4 * (h + pad[1]) + margins[1]/2

for x in range(4):
    for y in range(4):
        xpos = margins[0] + x * ( w + pad[0] ) - 0.5
        ypos = margins[1] + y * ( h + pad[1] ) - 0.5
        # remember: x is horizontal offset, y is vertical offset
        cards.append( { 'location' : { 'x' : xpos, 'y' : ypos },
                        'value' : 'A',
                        'size' : { 'x' : w, 'y' : h },
                        'face' : False,
                        'color' : '#990033',
                        'fill' : '#009933',
                        'fontcolor' : 'yellow',
                        'fontsize' : fontsize,
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
    
    # location of this card, set of points describing a rectangle
    loc = [
              ( x, y ),
              ( x, y+h ),
              ( x+w, y+h ),
              ( x+w, y),
          ] 
    # decoration on this card, set of points describing a diamond in the rectangle
    dec = [
              ( x + w/2, y ),
              ( x + w, y + h/2 ),
              ( x + w/2, y + h ),
              ( x, y + h/2 ),
          ]    
    tx = x + w/2 - card['fontsize']/4
    ty = y + h/2 + card['fontsize']/4
    canvas.draw_polygon(loc, card['linewidth'], card['color'], card['fill'])
    if card['face']:
        canvas.draw_text(str(card['value']), (tx,ty), card['fontsize'], card['fontcolor'])
    else:
        canvas.draw_polygon(dec, card['linewidth'], card['color'])
        canvas.draw_text("?", (tx, ty), card['fontsize'], card['color'])

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
        game['over'] = True
        animationtimer.start()
    
        
# helper function to initialize globals
def new_game():
    global animation_tick
    initialize_cards()
    game['draws'] = 0
    game['drawn'] = False
    game['match'] = False
    game['over'] = False
##   if showtimer.is_running(): showtimer.stop()
##   if matchtimer.is_running(): matchtimer.stop()
    if animationtimer.is_running(): animationtimer.stop()
    animation_tick = 0

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
##    if showtimer.is_running() or matchtimer.is_running() or animated: return
    if animated: return
    all = True
    for card in cards:
        if clicked(card,pos):
            card['face'] = True
            if game['drawn'] and game['match']:
                if game['drawn']['value'] != game['match']['value']:
                    game['drawn']['face'] = False
                    game['match']['face'] = False
                game['drawn'] = None
                game['match'] = None
            if not game['drawn']:
                game['drawn'] = card
            elif not game['match']:
                game['match'] = card
                game['draws'] += 1
        all = all and card['face']
    if all:
        if game['draws'] < game['best'] or game['best'] == 0: game['best'] = game['draws']
        for card in cards:
            card['drawn'] = False
        game['over'] = True
        animationtimer.start()
                
# cards are logically 50x100 pixels in size (or not, I set mine differently, above)    
def draw(canvas):
    global game_over
    for card in cards:
        draw_card(card,canvas)
    label.set_text("Turns = " + str(game['draws']))
    if game['best'] > 0:
        best.set_text("Best = " + str(game['best']))
    if game['over']:
        game_over_width = frame.get_canvas_textwidth(game_over_text, animation_tick)
        canvas.draw_text(game_over_text, ( canvaswidth/2 - game_over_width/2, 
                         canvasheight/2 ), animation_tick, "red" )
        if animation_tick >= fontsize*2:
            animationtimer.stop()

def animation():
    global animation_tick
    animation_tick += 1
    print animation_tick
    
def game_over():
    """Prematurely end the game for debugging"""
    for card in cards:
        card['drawn'] = False
    animationtimer.start()
    game['over'] = True

# create frame and add a button and labels
frame = simplegui.create_frame("Concentration", canvaswidth, canvasheight)
line = frame.add_label("----------------------------")
label = frame.add_label("Turns = 0")
best = frame.add_label("Best = 0")
line = frame.add_label("----------------------------")
frame.add_button("New Game", new_game)
line = frame.add_label("----------------------------")
#line = frame.add_label("----------DEBUGGING---------")
#frame.add_button("Show All", show_all)
#frame.add_button("Hide All", hide_all)
#frame.add_button("Animate", animation)
#frame.add_button("Game Over", game_over)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

##showtimer = simplegui.create_timer(showtime,hide_all)
##matchtimer = simplegui.create_timer(matchtime,hide_matches)
animationtimer = simplegui.create_timer(10,animation)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
