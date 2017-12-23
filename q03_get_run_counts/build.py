# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

def get_run_counts():

# You have been given the dataset already in 'ipl_df'.
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

    grouped_data = ipl_df[['runs']].groupby('runs')
    runs_count = grouped_data['runs'].count()
    return runs_count
# Solution

print get_run_counts()
