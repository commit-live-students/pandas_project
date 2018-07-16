# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    a = ipl_df[['match_code','runs']]
    return pd.pivot_table(a,'runs',aggfunc=np.count_nonzero,columns='runs',index = 'match_code')
