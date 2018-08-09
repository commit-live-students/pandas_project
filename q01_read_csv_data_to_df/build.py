# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = 'data/ipl_dataset.csv'

# Solution
def read_csv_data_to_df(path):
    ipl_data = pd.read_csv(path)
    return ipl_data

read_csv_data_to_df(path)


