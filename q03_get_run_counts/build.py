# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
def get_run_counts():
    runs_to_series = pd.Series(ipl_df['runs']) # Converts into pandas series
    unique_no_runs = np.unique(runs_to_series, return_counts=True) # Checks the unique values of how many 0,1,2,3,4,5,6
    array_to_series = pd.Series(data = unique_no_runs[1], index = unique_no_runs[0])
    return array_to_series

# Solution
print(get_run_counts())
