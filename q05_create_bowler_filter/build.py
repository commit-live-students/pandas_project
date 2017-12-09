# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
from pandas import Series, DataFrame

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def create_bowler_filter(bowler):
    b = ipl_df['bowler'] == bowler
    return b
