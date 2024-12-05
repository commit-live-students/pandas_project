# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import numpy as np
r=ipl_df['runs'].unique()
def get_runs_counts_by_match():
    a=ipl_df.pivot_table(index='match_code',columns='runs',aggfunc='count')
    return a['batsman']
get_runs_counts_by_match()


