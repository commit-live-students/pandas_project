# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

import pandas as pd

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    return pd.pivot_table(ipl_df, values = 'batsman', index='match_code', columns = ['runs'], aggfunc='count')
    #value synbolises the runs scored by batsman

#Call to the function
get_runs_counts_by_match()


