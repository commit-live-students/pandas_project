# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(some_value):
    df=ipl_df
    return df.loc[df['match_code'] == some_value]



df=ipl_df
some_value=598057
df
df.loc[df['match_code'] == some_value]



