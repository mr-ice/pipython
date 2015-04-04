# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

range_low = 0
range_high = 100
use_random_range = False
secret_number = None
guesses_remaining = 0

# helper function to start and restart the game
def new_game():
    global use_random_range
    if use_random_range:
        range_random()
    else:
        start_game()
        
def start_game():
    global range
    global guesses_remaining
    computer_guess()
    guesses_remaining = math.ceil(math.log(range_high-range_low+1,2))

    print "Guess a number between ",range_low,"and",range_high-1
    print "You have %d guesses remaining"%(guesses_remaining)
    frame.start()
    
def computer_guess():
    global secret_number
    global range_low
    global range_high
    secret_number = random.randrange(range_low,range_high)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_low
    global range_high
    global use_random_range
    use_random_range=False
    range_low=0
    range_high=100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_low
    global range_high
    global use_random_range
    use_random_range=False
    range_low=0
    range_high=1000
    new_game() 
    
def range_random():
    # button that changes the range to [x,y] and starts a game
    global range_low
    global range_high
    global use_random_range
    use_random_range=True
    range_low = random.randrange(0,1000)
    range_high = range_low + 100 + random.randrange(0,900)
    start_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global guesses_remaining
    try:
        guess = float(guess)
    except:
        print "Enter a number and try again"
        return
    else:
        print "You guessed",guess
        
        if guess == secret_number:
            print "Correct"
            new_game()
            return

        guesses_remaining -= 1
        if guesses_remaining <= 0:
            print "Sorry! You ran out of guesses, my number was %d, let's play again."%(secret_number)
            new_game()
            return

        if guess > secret_number:
            print "You have %d guesses remaining, my number is lower"%(guesses_remaining)
        else:
            print "You have %d guesses remaining, my number is higher"%(guesses_remaining)

            
# create frame
frame = simplegui.create_frame("Guess Number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100, 150)
frame.add_button("Range: 0 - 1000", range1000, 150)
frame.add_button("Range: x - y (both random)", range_random, 150)
frame.add_input("Guess: ",input_guess, 100)

# call new_game 

new_game()


# always remember to check your completed program against the grading rubric
