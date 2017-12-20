# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution

def read_csv_data_to_df(path):
    read_on = pd.read_csv(path)
    return (read_on)
print read_csv_data_to_df(path)
