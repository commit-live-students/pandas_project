# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution

def get_match_innings_runs():

    col_match_inn_runs =ipl_df[['match_code','inning','runs']]
    #print(col_match_inn_runs.head(5))
    grp_match_inn_runs=col_match_inn_runs.groupby(['match_code','inning']).sum()
    return grp_match_inn_runs
