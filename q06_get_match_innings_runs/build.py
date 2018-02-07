# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
#print ipl_df[:5]

# Solution
def get_match_innings_runs():
    innings_df = ipl_df[['match_code', 'inning', 'runs']]
    gb = innings_df.groupby( ['match_code', 'inning'])['runs'].sum()
    return gb
print get_match_innings_runs()
