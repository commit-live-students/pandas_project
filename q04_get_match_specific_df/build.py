# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(code):
    iplbool = ipl_df['match_code'] == code 
    return ipl_df[iplbool]

get_match_specific_df(598057)


