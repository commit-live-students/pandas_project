# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import pandas as pd
import numpy as np

def get_runs_counts_by_match():
    result = pd.pivot_table(ipl_df, 'batsman', ['match_code'],columns='runs',aggfunc='count')
    return result





