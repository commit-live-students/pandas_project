# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    ipl_df['scored_runs'] = ipl_df['runs']
    grouped = ipl_df.groupby (['match_code','scored_runs'])
    x = grouped.agg({'runs' : 'sum'}).reset_index()
    df = x.pivot_table(index = 'match_code', columns = ['scored_runs'], values = 'runs',aggfunc = np.sum)
    return df
    
