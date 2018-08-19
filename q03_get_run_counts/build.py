# %load q03_get_run_counts/build.py
# Default Imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_run_counts():
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
    runs_count = ipl_df['runs'].value_counts()
    count_series=pd.Series(runs_count)
    return count_series
# Solution
get_run_counts()


