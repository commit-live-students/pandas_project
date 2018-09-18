# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
import numpy as np
# Solution
def get_run_counts():
    
    unique,counts=np.unique(ipl_df['runs'].values,return_counts=True)
    d=dict(zip(unique,counts))
    runs_count=pd.Series(d)

    return runs_count


