# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
from pandas import Series
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_run_counts():
    s1 = Series(ipl_df['runs'])
    uniques = s1.value_counts(ascending=False)
    return uniques


