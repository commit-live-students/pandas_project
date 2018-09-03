# %load q07_get_run_counts_by_match/build.py
# Default Imports
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    match_code = list(set(ipl_df['match_code']))
    runs = list(set(ipl_df['runs']))
    #print(len(match_code))
    pivot_result = pd.pivot_table(ipl_df,values = 'win_type',index = 'match_code',columns = 'runs', aggfunc = 'count') 
    return pivot_result

get_runs_counts_by_match()


