# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df



# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

def get_match_innings_runs():
    #data.groupby(['col1', 'col2'])['col3'].mean()
    data = ipl_df.groupby(['match_code','inning'])['runs'].sum()
    #return ipl_df
    return data
# Solution
