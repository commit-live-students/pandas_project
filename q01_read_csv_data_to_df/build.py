# %load q01_read_csv_data_to_df/build.py

import pandas as pd

path = 'data/ipl_dataset.csv'

def read_csv_data_to_df(path):
    return pd.read_csv(path)




