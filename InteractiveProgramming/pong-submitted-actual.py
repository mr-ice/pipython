# Implementation of classic arcade game Pong
#

import simplegui
import random
import math

# initialize globals 
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PADDLE_VELOCITY = 4
BALL_VELOCITY = 4    # initially
LEFT = False
RIGHT = True


# Using more advanced data structures

# Game() holds scores and whether we are playing or not
# also defines how to draw the scores on the screen
class Game:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.score = [0, 0]
        self.playing = False

    def draw_scores(self,canvas):
        canvas.draw_text(str(self.score[0]),[200,80],30,"White")
        canvas.draw_text(str(self.score[1]),[385,80],30,"White")

# Ball() holds all the information about the ball, including
# how to determine if it hits surfaces or gutters.  Position
# and velocity of the ball are stored/manipulated here.
class Ball:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.v = [ 0, 0 ]
        
    def draw(self, canvas):
        canvas.draw_circle(
            [self.x, self.y],
            BALL_RADIUS,
            1,
            'White',
            'White')
        
    def wall(self): # horizontal surfaces
        if self.y < BALL_RADIUS or self.y > HEIGHT - BALL_RADIUS:
            self.v[1] = -self.v[1]
            
    def gutter(self):  # vertical surfaces
        return self.left_gutter() or self.right_gutter()
        
    def left_gutter(self):
        if self.x <= BALL_RADIUS+PAD_WIDTH:
            return True
        else:
            return False
        
    def right_gutter(self):
        if self.x >= WIDTH-PAD_WIDTH-BALL_RADIUS-1:
            return True
        else:
            return False

    def accelerate(self):
        # add 10% to the velocity of the ball
        self.v[0] *= 1.1
        self.v[1] *= 1.1

# A Paddle() holds the position and velocity of a paddle, and how
# to draw it.  It also has simple tests for collisions with walls
# and balls.
class Paddle:
    def __init__(self):
        self.height = PAD_HEIGHT
        self.reset()
        
    def reset(self, x = None):
        if x:
            self.x = x
        else:
            self.x = HALF_PAD_WIDTH
        self.y = HEIGHT/2 - HALF_PAD_HEIGHT
        self.v = 0
        
    def top(self):
        return self.y
    
    def bottom(self):
        return self.y + PAD_HEIGHT
       
    def draw(self, canvas):
        canvas.draw_line(
                [self.x, self.y],
                [self.x, self.y+PAD_HEIGHT],
                PAD_WIDTH,
                'White')

    def collide(self,ball):
        if ball.y > self.top() and ball.y < self.bottom():
            return True
        else:
            return False

    def wall(self):
        if self.y <= 0:
            self.v = 0
            self.y = 0
        if self.y > HEIGHT - PAD_HEIGHT:
            self.v = 0
            self.y = HEIGHT - PAD_HEIGHT

# create instances of our advanced data structures
game = Game()
ball = Ball()
# one paddle for each player
paddle = [ Paddle(), Paddle() ]


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global game,ball # these are vectors stored as listsr
    ball.reset()
    
    # using the randomization in the rubrick!
    # randomize pixels per second, then convert them to
    # pixels per tick (drawing layer ticks 60 times per second)
    x = random.randrange(120,240)/40
    y = random.randrange(60,180)/40

    # originally I just randomized the angle and left the
    # velocity fixed.  Since it speeds up on every hit I
    # thought this made for a better game.  There is a non
    # zero chance that on a serve (very fast) that your 
    # paddle will be too far out of position to move.  This 
    # happens much more with the higher speed given by the 
    # rubrick
    ##angle = random.randrange(10,56)
    ##x = math.cos(math.radians(angle)) * BALL_VELOCITY
    ##y = -math.sin(math.radians(angle)) * BALL_VELOCITY
    
    if direction != 'RIGHT':
        x = -x
        
    ball.v = [x,y]
    game.playing = True

# define event handlers
def new_game():
    global game, paddle, ball
    
    game.reset()
    paddle[0].reset()
    paddle[1].reset(WIDTH - HALF_PAD_WIDTH)
    direction = random.randrange(0,2)
    if direction < 1.0:
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")
        
def draw(canvas):
    global game, paddle, ball

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball.x += ball.v[0]
    ball.y += ball.v[1]

    ball.wall()  # handle top/bottom edges
    
    # draw ball
    ball.draw(canvas)
    
    # update paddle's vertical position, keep paddle on the screen
    paddle[0].y += paddle[0].v
    paddle[1].y += paddle[1].v
    
    paddle[0].wall()  # check/prevent running through walls
    paddle[1].wall()  # same with the other paddle
        
    # draw paddles
    paddle[0].draw(canvas)
    paddle[1].draw(canvas)
    
    # determine whether paddle and ball collide    
    if ball.gutter():  # left/right edges
        if ball.left_gutter():
            if paddle[0].collide(ball):
                ball.v[0] = -ball.v[0] * 1.1
            else:
                game.score[1] += 1
                spawn_ball("RIGHT") # whosoever shall score shall have ball coming at them
                
        if ball.right_gutter():
            if paddle[1].collide(ball):
                ball.v[0] = -ball.v[0] * 1.1
            else:
                game.score[0] += 1
                spawn_ball("LEFT") # whosoever shall score shall have ball coming at them

    # draw scores
    game.draw_scores(canvas)
        
def keydown(key):
    global paddle, game
    vel = PADDLE_VELOCITY
    if key == simplegui.KEY_MAP["up"]:
        paddle[1].v = -vel
    if key == simplegui.KEY_MAP["down"]:
        paddle[1].v = vel
    if key == simplegui.KEY_MAP["w"]:
        paddle[0].v = -vel
    if key == simplegui.KEY_MAP["s"]:
        paddle[0].v = vel
    if key == simplegui.KEY_MAP["space"] and not game.playing:
        direction = random.randrange(0,2)
        if direction < 1.0:
            spawn_ball("LEFT")
        else:
            spawn_ball("RIGHT")
    if key == 27 and game.playing:
        new_game()

def keyup(key):
    global paddle
    if key == simplegui.KEY_MAP["up"]:
        paddle[1].v = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle[1].v = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle[0].v = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle[0].v = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# Took this label out, while "Space" will still start a game
# the game according to the grading rubrick is also supposed 
# to spawn and start automatically :(
#frame.add_label("'Space' to start game")
frame.add_button("Reset",new_game)


# start frame
new_game()
frame.start()
