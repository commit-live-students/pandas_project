# %load q05_create_bowler_filter/build.py
# Default imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def create_bowler_filter(bowler):
    data= ipl_df['bowler']==bowler
    return data
create_bowler_filter('MM Patel')





