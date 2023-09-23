#!/usr/bin/python3
# character_roll.py
#
# Created by Persephone on 23.09.23 at 18.54
#

import dice
import pandas as pd
from random import randint
import argparse


# Read the file with the names
data_set = pd.read_csv("./data/baby-names.csv")

# Chooses only to use the names
names_ds = data_set[["name"]]


class Character():

    def __init__(self) -> None:
        pass

    def stats(self) -> int:
        l_stat = []
        for n in range(0,5):
            l_stat.append(randint(1,6))
        l_stat.sort()
        l_stat.pop(0)
        stat = sum(l_stat)
        return stat


    def name(self) -> str:
        rand_name = names_ds.loc[[randint(0,len(names_ds))]]
        name = str(rand_name)
        return name
    
    def race(self) -> str:
        races = ["Dwarf","Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-elf", "Half-orc", "Tielfling"]
        c_rase = races[randint(0,8)]
        return c_rase
    
    def character(self):
        c_dict = {
            "Name": [Character().name()],    
            "Race": [Character().race()],
            "STR": [Character().stats()],
            "DEX": [Character().stats()],
            "CON": [Character().stats()],
            "INT": [Character().stats()],
            "WIS": [Character().stats()],
            "CHA": [Character().stats()],
            }
        c_dataframe = pd.DataFrame(c_dict)
        return c_dataframe



def main():
    if args.character:
        for n in range(0,args.reroll):
            print(Character().character())
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='Basic Character Information',
            description='Returns a random character with a name, race and base stats')
    parser.add_argument('character', action='store_true', help='Get a random character')
    parser.add_argument('-r', '--reroll', type=int, default=1, help='Get more characters at once.')

    args = parser.parse_args()
    main()
