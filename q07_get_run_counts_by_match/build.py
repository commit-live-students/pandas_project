# %load q07_get_run_counts_by_match/build.py
# Default Imports
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_runs_counts_by_match():
    df1=ipl_df[['match_code','runs']]
    df=pd.pivot_table(df1,index='match_code',columns='runs',aggfunc=len)
    return df



