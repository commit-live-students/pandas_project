# %load q06_get_match_innings_runs/build.py
# Default Imports
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
def get_match_innings_runs():
    Innings_Scores = ipl_df.groupby(
        ['match_code','inning','runs'])['runs'].sum()
    return Innings_Scores



