# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
# Solution
def create_bowler_filter(bowler):
    '''Solution 1
    div = lambda x: x == ipl_df['bowler'][:]
    return div(bowler)'''
    #Solution 2:
    return (ipl_df['bowler']==bowler)
#create_bowler_filter('I Sharma')




