# guessing_game.py
# This program implements a simple binary search algorithm for guessing a user
# input number within a range.

# Author: Oguntuase Victor. A
# email: freelanceel0@gmail.com
from art import *
import math

# functions
def initialize():
    tprint("Guessing Game".center(100,' '))    # Printing Ascii text

    Description = """\n\t\t\tThis game guesses your choice of a number within a range. You may set the upper limit, but the lower limit is 0 by default.\
    \n\t\t\tUpon deciding the upper limit, you are to choose a number between 0 and that upper limit.\n\
    \n\n\t\t\tUse "Y","N","H", and "L" for guiding the computer to your guess. Be truthful about the response, else this won't work!\n\n"""

    print(Description)

# The search and algorithm implementation
def play():
    # Required
    upper_limit = int(input("Enter the maximum number/upper limit: "))
    lower_limit = 0    #initial lower bound

    if (lower_limit == upper_limit):
        return print(f"\nYou shouldn't use the same lower and upper limit Genius! The answer is obviously {lower_limit}! Exiting, because you suck!")
    else:
        expected_trials = round(math.log2(upper_limit))
        guess = 0
        trials = 0
        print(f"\nThis should take no more than {expected_trials} guesses, at worst. Unless you are not truthful at some point in the game! \n\n")

        while (trials < expected_trials):
            trials += 1
            guess = math.floor((lower_limit + upper_limit)/2)
            print(f"\n\nGuess {trials}: {guess}\n")
            check1 = input("Is that the correct guess? Use 'Y' or 'N' to answer accordingly: ").upper()
            if (check1 == "N"):
                check2 = input("Is the guess Higher than your choice or Lower? Use 'H' or 'L' to answer accordingly: ").upper()
                if (check2 == "L"):
                    lower_limit = guess + 1
                elif (check2 == "H"):
                    upper_limit = guess - 1
                else:
                    return print("\n\nYou entered an incorrect choice. Be it on purpose or otherwise, I am exiting anyway!\n")



            else:
                return print(f"\n\nExcellent, I have successfully guessed your number '{guess}' in {trials} trials, as promised!\nExiting Now !!\n")
        else:
            return print("\n\nYou must have lied to me at some point. Have a good day, you lying @$%%^#%$^&&%$^%& bleep bleep ...\n")

# Initializing
initialize()
play()
















