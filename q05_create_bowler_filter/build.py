# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
from pandas import Series
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def create_bowler_filter(bowler):
    #print ipl_df
    bowlers = ipl_df['bowler']
    #print bowlers
    bowler = np.where((bowlers==bowler),True,False)
    bowler = Series(bowler)
    return bowler


