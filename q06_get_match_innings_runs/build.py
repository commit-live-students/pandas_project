#%load q06_get_match_innings_runs/build.py
import pandas as pd
import numpy as np

ifl_df=pd.read_csv('./data/ipl_dataset.csv')

def get_match_innings_runs():

    ifl_df2=ifl_df.groupby(['match_code','inning'])['runs'].sum()

    return ifl_df2




