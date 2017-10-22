# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

def get_match_innings_runs():
    data=ipl_df.groupby(['inning','match_code']).sum()['runs']
    return data
get_match_innings_runs()
