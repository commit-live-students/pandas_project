# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

# You have been give the dataset aaggfunc=nc=nc=nc=ady in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():
    new_data = DataFrame(ipl_df[['match_code', 'runs']].groupby(['match_code','runs'])['runs'].count())
    new_data.columns = ['Total_runs']
    return new_data.pivot_table(index='match_code', columns='runs',values='Total_runs')

print get_runs_counts_by_match()
