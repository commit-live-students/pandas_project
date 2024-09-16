# %load q07_get_run_counts_by_match/build.py
# Default Imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
def get_runs_counts_by_match(): 
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
    runs_df = ipl_df.pivot_table(columns=['runs'],aggfunc=len,index=['match_code'],values=['total'])
    return runs_df
# Solget_runs_counts_by_matchution
get_runs_counts_by_match()

