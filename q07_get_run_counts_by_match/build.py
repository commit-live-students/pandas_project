# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

import numpy as np
import pandas as pd
def get_runs_counts_by_match():
    ipl_df['count']=1
    data_pivot=ipl_df.pivot_table('count',index='match_code',columns='runs',aggfunc=np.size)
    return data_pivot
