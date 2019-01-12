# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(match_code):
    s = pd.Series()
    s = ipl_df.loc[ipl_df['match_code'] == match_code]
    return s
type(ipl_df['match_code'])
ipl_df.loc[ipl_df['match_code'] == 392203]

get_match_specific_df(598057)





