#%load q05_create_bowler_filter/build.py
import pandas as pd
import numpy as np

ifl_df=pd.read_csv('./data/ipl_dataset.csv')

def create_bowler_filter(bowler):

    bl=ifl_df['bowler']

    return bl==bowler


    


