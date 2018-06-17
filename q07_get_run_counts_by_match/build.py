# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match(bowler='I Sharma'):
    ipl_df1 = pd.read_csv('./data/ipl_dataset.csv',index_col='match_code')
    ipl_df2 = ipl_df.pivot_table(columns='runs', index='match_code',aggfunc='sum', values = 'batsman')
    
    return ipl_df2

get_runs_counts_by_match(bowler='I Sharma').shape
get_runs_counts_by_match()

