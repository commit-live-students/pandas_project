# Default imports
import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    filter1 = ipl_df['match_code'].astype(np.int64) == match_code
    df = ipl_df[filter1]
    return df
