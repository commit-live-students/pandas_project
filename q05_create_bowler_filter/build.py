# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
import pandas as pd
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def create_bowler_filter (bowler):
    filterData = [Filterspecific(row,bowler) for row in ipl_df['bowler']]
    return pd.Series(filterData)

def Filterspecific (row,bowler):
    return row == bowler

# create_bowler_filter('I Sharma').sum()


