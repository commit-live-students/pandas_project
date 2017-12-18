# Default Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    runs_frequency = ipl_df.pivot_table('inning', aggfunc=np.count_nonzero, index='match_code', columns='runs')
    return runs_frequency
