#-*- coding: UTF-8 -*-
#dice rolling simulator
from random import randint
from sys import exit
import os

os.system('clear')
print "Welcome to the dice rolling simulator!"
raw_input("Press enter to begin.")

def roll():
    os.system('clear')
    die1 = randint(1, 6)
    """die2 = randint(1, 6)
    global total
    total = die1 + die2
    storetotal()
    """
    print "您投掷的骰子是%d" % (die1)
    print "\n\nRoll again?"
    roll_again = raw_input("Press enter to roll again, type 'stats' to view scores, or 'quit' to exit.\n> ")    
    if roll_again == "":
        roll()
    elif roll_again == "stats":
        stats()
    elif roll_again == "quit":
        exit(0)
    else:
        print "I don't know what that means so you get to roll again."
        raw_input("> ")
        roll()
        
roll()
