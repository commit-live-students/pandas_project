# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

def get_runs_counts_by_match():
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

    return ipl_df.pivot_table(columns=ipl_df['runs'],index=ipl_df['match_code'],aggfunc='count').iloc[:,:7]

get_runs_counts_by_match()



