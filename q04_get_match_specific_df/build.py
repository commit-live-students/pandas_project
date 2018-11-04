# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(match_code):
    return ipl_df.loc[ipl_df['match_code'].isin([match_code])]

match_code = 598057
expected_shape = (241,24)
actual_shape = get_match_specific_df(match_code).shape
actual_shape



