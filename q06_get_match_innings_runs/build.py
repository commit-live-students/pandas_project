# Default Imports
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    matchcode_innings_runs=ipl_df[['match_code','inning','runs']]
    inning_group=matchcode_innings_runs.groupby('inning')
    inning_group_sum=inning_group['runs'].sum()
    return inning_group_sum
