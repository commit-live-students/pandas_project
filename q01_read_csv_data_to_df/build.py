# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv"

# Solution

def read_csv_data_to_df(path):
    DataFrame = pd.read_csv(path)
    return DataFrame
print read_csv_data_to_df(path)
