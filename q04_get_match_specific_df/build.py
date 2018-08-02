# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(matchcode):
    df=ipl_df
    for x in df['match_code']:
        if x==matchcode:
            return df.loc[df['match_code']==matchcode]


a=get_match_specific_df(598057)

a.shape


