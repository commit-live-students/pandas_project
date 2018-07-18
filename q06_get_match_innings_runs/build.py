# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.

def get_match_innings_runs():
    ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
    return ipl_df.groupby(['match_code','inning'])['runs'].sum()


# Solution
