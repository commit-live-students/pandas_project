# %load q07_get_run_counts_by_match/build.py
# Default Imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    data = ipl_df.loc[:,['match_code', 'runs']]
    runs = ipl_df.loc[:,'runs']
    pivot_data = pd.pivot_table(data, index = 'match_code',
                        columns = runs, aggfunc = 'count')
    return pivot_data

print (get_runs_counts_by_match())


