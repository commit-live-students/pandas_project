# Default Imports
import pandas as pd
from pandas import Series, DataFrame
# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path, dtype=str):
    df = pd.read_csv(path, header=0)
    return df
