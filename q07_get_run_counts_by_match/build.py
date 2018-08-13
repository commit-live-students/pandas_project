# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_runs_counts_by_match():
    # Solution
    updated_ipl_df = ipl_df[['match_code', 'runs']]
    df = pd.pivot_table(updated_ipl_df, index='match_code', columns=['runs'], values=['runs'], aggfunc=lambda x: len(x), fill_value = 0)
    return df
    
get_runs_counts_by_match()


