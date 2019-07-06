# %load q05_create_bowler_filter/build.py
# Default imports
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
bowler = 'I Sharma'
# Solution
def create_bowler_filter(bowler):
    bool_series = ((ipl_df['bowler']==bowler))==True
    return bool_series.where(bool_series==True)



