# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_run_counts():
    runs = ipl_df['runs']
    count = runs.value_counts()
    return Series(count)
get_run_counts()
