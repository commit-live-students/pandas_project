# Default Imports
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    match_group = pd.DataFrame(ipl_df[['match_code', 'runs']].groupby(['match_code', 'runs'])['runs'].count())
    match_group.columns = ['total_runs']
    return pd.pivot_table(match_group, index = 'match_code', columns = 'runs', values = ['total_runs'])

    #return match_group
print get_runs_counts_by_match()
