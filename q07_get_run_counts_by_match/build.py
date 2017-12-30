# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    df = ipl_df.pivot_table(values='inning',columns=['runs'],index=['match_code'],aggfunc=np.count_nonzero)
    return df
