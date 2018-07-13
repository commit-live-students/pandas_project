# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

def read_csv_data_to_df(p):
    df=pd.read_csv(p)
    return df

read_csv_data_to_df(path)
