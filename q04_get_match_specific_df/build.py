# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd

match_code = 392203

def get_match_specific_df(match_code):
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

    match_int=pd.Series(data=ipl_df['match_code'], dtype='int32')

    return ipl_df[match_int == match_code]

get_match_specific_df(match_code)







