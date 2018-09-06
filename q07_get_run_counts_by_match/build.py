# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    ipl_df['runs_by_bt']=ipl_df['runs']
    df=pd.pivot_table(ipl_df,values='runs',index=['match_code'],columns='runs_by_bt',aggfunc={'runs':'count'})
    return df


