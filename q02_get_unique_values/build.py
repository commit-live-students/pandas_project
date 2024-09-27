#%load q02_get_unique_values/build.py

import pandas as pd

path='./data/ipl_dataset.csv'

def get_unique_venues():
    df=pd.read_csv(path)

    venue=df.venue.unique()

    return venue






