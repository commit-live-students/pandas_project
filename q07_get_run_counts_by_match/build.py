# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match(bowler = 'I Sharma'):
    ipl_df = pd.read_csv('./data/ipl_dataset.csv',index_col = 'match_code')
    df = ipl_df.pivot_table(columns = 'runs', aggfunc='sum', index = 'match_code', values = 'batsman')
    return df
get_runs_counts_by_match(bowler = 'I Sharma')

