# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
# Solution

def get_run_counts():
    d=(ipl_df['runs'])
    
    unique, counts = np.unique(d, return_counts=True)
    
    pf=pd.Series(counts,index=unique)
    return(pf)


