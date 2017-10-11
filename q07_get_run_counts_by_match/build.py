# %load q07_get_run_counts_by_match/build.py
# Default Imports
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():
    pivot_df = ipl_df.pivot_table(
                values='runs',
                index='match_code',
                columns=ipl_df['runs'],
                aggfunc='count')
    return pivot_df
