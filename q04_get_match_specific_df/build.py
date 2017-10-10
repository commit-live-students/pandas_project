# %load q04_get_match_specific_df/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
#ipl_df['match_code']
def get_match_specific_df(match_code):
    fil1=ipl_df['match_code']==match_code
    return ipl_df[fil1]

#GET_MATCH_SPECIFIC_DF(392203)
