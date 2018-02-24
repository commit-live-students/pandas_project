# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(filepath):
    data = pd.read_csv(filepath)
    #print type(data)
    return data

read_csv_data_to_df(path)
