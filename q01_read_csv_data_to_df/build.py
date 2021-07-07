# %load q01_read_csv_data_to_df/build.py
# Default Imports
import pandas as pd
import csv


# Path has been given to you already to use in function.
path = 'data/ipl_dataset.csv'

# Solution
def read_csv_data_to_df(path):
    
    df1 = pd.read_csv(path)
    df=pd.DataFrame(df1)
    return df



read_csv_data_to_df(path)








