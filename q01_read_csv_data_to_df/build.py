# Default Imports
import pandas as pd

# Path has been given to you already to use in function.

def read_csv_data_to_df(path):
    path = "data/ipl_dataset.csv"
    df = pd.read_csv(path,dtype ='str')
    return df
