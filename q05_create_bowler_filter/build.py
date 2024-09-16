# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
bowler = 'I Sharma'
def create_bowler_filter(bowler):
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
    return ipl_df['bowler'] == bowler

create_bowler_filter(bowler)


