# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
def get_match_innings_runs():
    df1 = ipl_df.loc[:,['match_code', 'inning', 'runs']]
    df2 = df1.groupby(['match_code', 'inning']).sum()
    return df2
    





print (get_match_innings_runs())



