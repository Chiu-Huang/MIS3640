# Q5
# You need to replace 'pass' with your code
# I adjusted line 65 to represent whoever takes the last pebble will lose as the problem states so


from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)


def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    pile = randint(10,100)
    turn = randint(0,1)
    strategy = randint(0, 1)
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                take = 1 
                # Take the last marble.
            elif strategy == DUMB:
                take = randint(1,pile//2)
                # Take a random, legal number of marbles from the pile.
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                take = randint(1,pile//2)
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
            else:
                n = 0
                while not (pile >= 2**n and pile < 2**(n+1)):
                    n += 1
                take = pile - 2**n + 1                      
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
            pile -= take
            # Update pile
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN
        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")
            take = int(input("How many marbles will you take? "))
            while (take > max (1,pile/2)): 
                take =  int (input("invalid input, please re-enter the marbles that you will take? between 1 and {} ".format(pile//2) ))
            # Force the user to take a legal number of marbles.
            pile -= take
            # Update pile
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER
    return turn == HUMAN

if nim():
    print("You Won!")
else:
    print("The computer won!")
