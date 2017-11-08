# %load q04_get_match_specific_df/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")


def get_match_specific_df(match_code):
    ipl_df['match_code'] = ipl_df.match_code.astype(str)
    new_df = ipl_df.set_index('match_code')
    match = str(match_code)
    df = new_df.loc[match]
    return df







# Solution
