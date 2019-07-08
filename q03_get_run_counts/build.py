# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import pandas as pd
def get_run_counts():
    runs=ipl_df['runs']
    freq_runs=[0]*7
    for run in runs:
        freq_runs[run]+=1
    count_runs=pd.Series(freq_runs)
    return count_runs


