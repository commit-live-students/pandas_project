# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = 'data/ipl_dataset.csv'
ipl = pd.read_csv(path)

# Solution
def read_csv_data_to_df(path):
    return pd.DataFrame(pd.read_csv(path))






