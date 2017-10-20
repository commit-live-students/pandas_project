# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    filtered_data = ipl_df[['match_code','inning','runs']]
    return filtered_data.groupby(['match_code','inning']).sum()
print get_match_innings_runs()
