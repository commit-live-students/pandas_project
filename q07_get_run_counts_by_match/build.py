# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    
    # create new dataframe of following columns
    ipl_df1 = ipl_df[['match_code','runs','batsman']]
    
    # create a pivot table 
    pivot_df = pd.pivot_table(ipl_df1, values = ['runs'], index = ['match_code'], columns = ['runs'], aggfunc = 'count')
    
    return pivot_df
get_runs_counts_by_match()



