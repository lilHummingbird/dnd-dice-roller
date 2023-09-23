#!/usr/bin/python3
# enemy.py
#
# Created by Persephone on 21.09.23 at 16.40
#

import pandas as pd
from random import randint
import argparse

# Insert data from data.csv
data_set = pd.read_csv("./data/data.csv")

# Takes out unecessary info and returns useful info
refined_ds = data_set[["Name", "AC", "HP", "Speeds", "STR", "DEX", "CON", "INT", "WIS", "CHA", "CR"]]

# Callable stuff
def rand_enemy():

    # Chooses a random row in the document
    rand_row = refined_ds.loc[[randint(0,801)]]

    result = rand_row
    return result

def main():
    if args.enemy:
        for n in range(0,args.reroll):
            print(f"Your random enemy:\n{rand_enemy()}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="Random Enemy",
            description="Gives you a random enemy from the provided data file.")
    parser.add_argument('enemy', action='store_true', help='Get a random enemy from the provided dataset')
    parser.add_argument('-r','--reroll',type=int, default=1, help='Repeat the diceroll x amount of times')

    args = parser.parse_args()

    main()
