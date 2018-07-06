# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
from collections import defaultdict
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    df1 = pd.pivot_table(data=ipl_df.loc[:,['match_code', 'runs']], index='match_code', columns=ipl_df.loc[:,'runs'], aggfunc='count')
    return df1
