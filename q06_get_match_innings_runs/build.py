# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    ipl_df_new = ipl_df[['match_code','inning','runs']]
    group = ipl_df_new.groupby(['match_code','inning'], as_index=['match_code','inning']).sum()
    return group

#print get_match_innings_runs()
