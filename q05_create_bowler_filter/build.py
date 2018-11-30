# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
ipl_df
# Solution
def create_bowler_filter(b):
    a=pd.Series(ipl_df['bowler']==b)
    return a
create_bowler_filter('I Sharma')

