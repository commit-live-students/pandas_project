# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = 'data/ipl_dataset.csv'

# Solution
def read_csv_data_to_df(path):
    ipl_df = pd.read_csv(path)
    print(ipl_df)
    print(ipl_df.shape)
    return ipl_df
    return ipl_df.shape
read_csv_data_to_df(path)



