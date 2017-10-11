# %load q03_get_run_counts/build.py
# Default Imports
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_run_counts():
    runs=ipl_df['runs'].value_counts()
    return runs
