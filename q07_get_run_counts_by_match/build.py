# %load q07_get_run_counts_by_match/build.py
# Default Imports
import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df


# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
def get_runs_counts_by_match():
    df1 = ipl_df[['match_code','runs']]
    table = pd.pivot_table(df1,values = 'runs',columns = ipl_df['runs'], index= ['match_code'],fill_value=0, aggfunc='count')
    return table
# Solution
