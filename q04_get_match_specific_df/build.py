# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(match_code):
    match_code = int(match_code)
    new_ipl_df = ipl_df[ipl_df['match_code']==match_code]
    return new_ipl_df



# Solution







