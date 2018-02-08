# Default Imports
import pandas as pd
from pandas import DataFrame

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path=path):
    df = pd.read_csv(path)
    return df

#print read_csv_data_to_df(path)
