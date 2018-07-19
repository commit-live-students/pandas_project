# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
import pandas as pd
import numpy as np

# Solution

def get_match_innings_runs():
    ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
    df = ipl_df.groupby('match_code').agg(np.sum)
    return df['runs']

get_match_innings_runs()

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
import pandas as pd
import numpy as np

# Solution

def get_match_innings_runs():
    ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
    df = ipl_df.groupby('match_code').sum()
    return df[['runs']]

get_match_innings_runs()

