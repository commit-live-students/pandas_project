# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd
path = "data/ipl_dataset.csv"


def read_csv_data_to_df(path):
# Path has been given to you already to use in function.
    df = pd.read_csv(path)
    return df
# Solution
