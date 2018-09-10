# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
import numpy as np
# Solution
def get_runs_counts_by_match():
    my_df = ipl_df.groupby('match_code')['runs'].value_counts().unstack().fillna(0)
    return pd.pivot_table(my_df,index=['match_code'])
#get_runs_counts_by_match()






