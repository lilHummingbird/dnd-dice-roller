#!/usr/bin/python3
# dice.py
#
# Created by Persephone on 21.09.23 at 16.07
#
from random import randint
import argparse

class Dice():
    """
    This class represents any kind of die.
    Just specify the amount of sides in the constructor

    And use `self.roll()` to roll the die
    """

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        result = randint(1, self.sides)
        return result
 
def rolldice(x):
    result = Dice(x).roll()
    return result

def main():
    if args.sides:
        print("Your roll was:\n")
        for n in range(0,args.reroll):
            print(f"{rolldice(args.sides)}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='Dice roller',
            description='Rolls dice')
    parser.add_argument('sides', type=int, help='Choose to roll dice with x sides.')
    parser.add_argument('-r','--reroll',type=int, default=1, help='Repeat the diceroll x amount of times')
    args = parser.parse_args()

    main()
