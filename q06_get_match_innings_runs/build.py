# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

def get_match_innings_runs():
    ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

    return ipl_df['runs'].groupby([ipl_df.match_code,ipl_df.inning]).agg(np.sum)

get_match_innings_runs()






