# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path):
    rcsv = pd.read_csv(path)
    print type(rcsv)
    return rcsv

read_csv_data_to_df(path)
