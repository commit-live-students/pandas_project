# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_runs_counts_by_match():
    
    
    data = ipl_df.loc[:, ['runs']]   
    df = data.pivot_table(data, aggfunc=np.sum, index=ipl_df.loc[:,'match_code'], columns=ipl_df.loc[:,'runs'])
    return df

