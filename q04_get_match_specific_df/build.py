# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_match_specific_df(match_code):
    ipldf1=ipl_df[ipl_df['match_code']==match_code]
    return ipldf1
    get_match_specific_df('392203')


