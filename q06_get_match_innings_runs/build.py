# %load q06_get_match_innings_runs/build.py
# Default Imports
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution

def get_match_innings_runs():
    data=ipl_df.groupby(['inning','match_code'])
    return data['runs'].agg([np.sum])
    
#print(get_match_innings_runs().sum())





