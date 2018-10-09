# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

import pandas as pd
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
def get_runs_counts_by_match():
    runs_per_match=ipl_df.pivot_table(values='batsman',index=['match_code'],columns=('runs'),aggfunc='count')
    #value synbolises the runs scored by batsman
    return runs_per_match
get_runs_counts_by_match()



