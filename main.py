#!/usr/bin/python3
#  main.py
#
#  Created by Persephone on 21.09.23 at 16.05
#

import dice
from enemy import rand_enemy
from character_roll import Character
import argparse

def main():
    if args.dice:
        print("Your roll was:")
        for n in range(0,args.reroll):
            print(dice.rolldice(args.dice))
    elif args.enemy:
        print("Your enemies are:")
        for n in range(0,args.reroll):
             print(rand_enemy())
    elif args.character:
        print("Your characters are:")
        for n in range(0,args.reroll):
            print(Character().character())



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='DM Tools',
            description='A set of tools you can run from the command line during your games of DND for quick access to basic functions.',)
    parser.add_argument('-d', '--dice', type=int, help='Choose to roll a dice', choices=[20, 12, 100, 10, 8, 6, 4, 2])
    parser.add_argument('-r','--reroll',type=int, default=1, help='Repeat the diceroll x amount of times')
    parser.add_argument('-e', '--enemy', action='store_true', help='Get a random enemy from the dataset')
    parser.add_argument('-c', '--character', action='store_true', help='Get a random character')




    args = parser.parse_args()


    main()
