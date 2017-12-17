# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
from pandas import DataFrame

def get_runs_counts_by_match():
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    a = ipl_df.pivot_table(index=['match_code'],columns=['runs'], aggfunc='count') #[:,[0,1,2,3,4,5,6]]
    return a.iloc[:,[0,1,2,3,4,5,6]]
