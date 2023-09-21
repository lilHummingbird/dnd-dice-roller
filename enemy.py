#
# enemy.py
#
# Created by Persephone on 21.09.23 at 16.40
#

import pandas as pd
from random import randint

# Insert data from data.csv
data_set = pd.read_csv("data.csv")

# Takes out unecessary info and returns useful info
refined_ds = data_set[["Name", "AC", "HP", "Speeds", "STR", "DEX", "CON", "INT", "WIS", "CHA", "CR"]]

# Callable stuff
def rand_enemy():

    # Chooses a random row in the document
    rand_row = refined_ds.loc[[randint(0,801)]]

    result = rand_row
    return result
