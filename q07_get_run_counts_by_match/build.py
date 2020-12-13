# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    a= ipl_df[['match_code','runs','batsman']]
    b= pd.pivot_table(a, values=['runs'], index=['match_code'],columns=['runs'],aggfunc= 'count')
    return b
    
get_runs_counts_by_match()



