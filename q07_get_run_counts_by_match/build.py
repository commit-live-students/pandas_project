# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
import pandas as pd
import numpy as np

def get_runs_counts_by_match():
    ipl_df.insert(0, column='freq', value=np.int16(1)) # add freq column
    mypivot = pd.pivot_table(ipl_df, index='match_code', columns='runs', values='freq'
                             , fill_value=0, aggfunc=len)
    return mypivot
#print get_runs_counts_by_match()
