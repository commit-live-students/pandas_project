# Default Imports
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution

# Solution

def read_csv_data_to_df (path):
    ipl_matches_array =pd.read_csv(path, delimiter=",")
    df_ipl_matches = DataFrame(ipl_matches_array)
    return df_ipl_matches
