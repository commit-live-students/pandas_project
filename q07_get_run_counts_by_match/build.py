# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import numpy as np
import pandas as pd
def get_runs_counts_by_match():
    r=ipl_df.pivot_table(index=['match_code'],columns=['runs'],fill_value=0,aggfunc='count')
    return r



