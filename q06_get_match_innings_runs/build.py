# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    to_drop = ['win_margin','delivery','extras','total']
    ipl_2 = ipl_df.groupby(['match_code','inning']).sum()
    ipl_2.drop(to_drop, axis = 1, inplace=True)
    return ipl_2
get_match_innings_runs()
