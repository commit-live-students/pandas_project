# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    df = ipl_df[ipl_df['match_code'] == 392203]
    return df
print get_match_specific_df(match_code = 392203)
