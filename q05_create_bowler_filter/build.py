# Default imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
bowler = 'I Sharma'
def create_bowler_filter(bowler):
    bowler_names=ipl_df['bowler']
    bowler_series=Series(bowler_names,dtype=np.str)
    true_false_bowler_series=(bowler_series==bowler)
    return true_false_bowler_series
