# Default Imports
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():

    d1 = ipl_df[['match_code','inning','runs']]
    d2 = d1.groupby(['match_code','inning'])
    df = d2['runs'].sum()

    return df

print get_match_innings_runs()
