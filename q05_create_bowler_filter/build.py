# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
# Solution
def create_bowler_filter(bowler):
    bowler_filter = pd.Series(ipl_df['bowler']==bowler) 
    return bowler_filter




