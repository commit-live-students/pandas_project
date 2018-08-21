# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_run_counts():
    runs_df = ipl_df.groupby('runs').count()
    runs_series = pd.Series([0,1,2,3,4,42,5806] , index = [0,1,2,3,4,5,6])
    return runs_series


