#%load q06_get_match_innings_runs/build.py# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

import numpy as np
# Solution
def get_match_innings_runs():
    a=ipl_df.groupby(by=['match_code','inning']).agg(np.sum)
    return a[['runs']]
get_match_innings_runs()

# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

import numpy as np
# Solution
def get_match_innings_runs():
    a=ipl_df.groupby(by=['match_code','inning']).agg(np.sum)
    return a[['runs']]
get_match_innings_runs()


