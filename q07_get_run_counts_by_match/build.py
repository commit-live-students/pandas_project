# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    pivot_df = ipl_df.pivot_table(
                values='inning',      # We want to aggregate the values of which column?
                index='match_code',       # We want to use which column as the new index?
                columns=['runs'],
                aggfunc='count')
    return pivot_df


