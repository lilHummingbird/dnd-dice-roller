#!/usr/bin/python3
# encounter.py
#
# Created by Persephone on 23.09.23 at 23.32
#

from random import randint
import argparse

class Encounter():
    def place(self) -> str:
        places = ["Mountain","Field", "Catacombs", "Dungeon", "Forest","Village","Riverside","Underwater cave"]
        rand_place = places[randint(0,7)]
        return rand_place

    def health(self) -> str:
        health = ["Super health", "Bad health", "Mediocre health", "Good health", "Subpar health"]
        rand_health = health[randint(0,4)]
        return rand_health

    def enemy(self) -> str:
        enemies = ["Bats", "Black bears", "Goblins", "Bandits", "Ghouls", "Bullywugs","Magmin","Scarecrow"]
        rand_enemy = enemies[randint(0,7)]
        return rand_enemy
    
    def encounter(self) -> str:
        return f"The party is in a {Encounter().place()} in {Encounter().health()}, facing {randint(1,10)} {Encounter().enemy()}."

def main():
    if args.encounter:
        for n in range(0,args.reroll):
            print(Encounter().encounter())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='Random Encounter Generator',
            description='Generates a random encounter.')
    parser.add_argument('encounter', action='store_true', help='Get a random encounter generated')
    parser.add_argument('-r','--reroll', type=int, default=1, help='Repeat')

    args = parser.parse_args()
    main()
