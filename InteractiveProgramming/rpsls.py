# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

choices = list(( 'rock', 'Spock', 'paper', 'lizard', 'scissors' ))

# helper functions

def name_to_number(name):
    """ convert name to number using if/elif/else
    don't forget to return the result!"""
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "ERROR, invalid name"
        quit()
    # Alternately, using my list above I could just use a simple
    # list method to find the number.  This code is never run.
    try:
        return choices.index(name)
    except:
        print "Invalid Name"
        quit()
       
def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid Number"
        quit()

    # Alternately, using my list above I could just use a simple
    # list feature to find the name.  This code is never run.
    try:
        return choices[number]
    except:
        print "Invalid Number"
        quit()
        

def difference(pname,cname):
    # Convert both to a number and return difference modulo five
    return (name_to_number(pname)-name_to_number(cname))%5

def result(player_choice,comp_choice):
    diff = difference(player_choice,comp_choice)
    if diff == 0:
        return "Tie"
    elif diff == 1 or diff == 2:
        return "Player"
    elif diff == 3 or diff == 4:
        return "Computer"
    else:
        return "Illogical, Spock wins!"

def rpsls(player_choice): 
    # print out the message for the player's choice
    print "Player chooses %s" %(player_choice)    

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses %s" %(comp_choice)
    
    # compute difference of comp_number and player_number modulo five
    differs = difference(player_choice,comp_choice)
        
    # use if/elif/else to determine winner, print winner message
    if differs == 0:
        print "Player and computer tie!"
    elif differs == 1 or differs == 2:
        print "Player wins!"
    elif differs == 3 or differs == 4:
        print "Computer wins!"
    else:
        print "Nobody wins because I'm bad at math!"
    
    # print a blank line to separate consecutive games
    print ""
    

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# always remember to check your completed program against the grading rubric

#print "P","C","D","R"
#for x in choices:
#    for y in choices:
#        print x,y,difference(x,y),result(x,y)
#
#P C D R
#rock rock 0 Tie
#rock Spock 4 Computer
#rock paper 3 Computer
#rock lizard 2 Player
#rock scissors 1 Player
#Spock rock 1 Player
#Spock Spock 0 Tie
#Spock paper 4 Computer
#Spock lizard 3 Computer
#Spock scissors 2 Player
#paper rock 2 Player
#paper Spock 1 Player
#paper paper 0 Tie
#paper lizard 4 Computer
#paper scissors 3 Computer
#lizard rock 3 Computer
#lizard Spock 2 Player
#lizard paper 1 Player
#lizard lizard 0 Tie
#lizard scissors 4 Computer
#scissors rock 4 Computer
#scissors Spock 3 Computer
#scissors paper 2 Player
#scissors lizard 1 Player
#scissors scissors 0 Tie

