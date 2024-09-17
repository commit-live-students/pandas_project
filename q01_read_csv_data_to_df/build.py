# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = 'data/ipl_dataset.csv'
def read_csv_data_to_df(path):
    data = pd.read_csv(path)
    print (data.head())
    return data
# Solution

print (read_csv_data_to_df(path))


