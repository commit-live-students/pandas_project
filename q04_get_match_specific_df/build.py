# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(match_code):
    if type(match_code) == int:
        return ipl_df[ipl_df['match_code'] == match_code]
    else:
        print('Match code is not an int')

get_match_specific_df(392203)
    



