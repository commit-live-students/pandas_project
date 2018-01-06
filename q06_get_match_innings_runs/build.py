import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
def get_match_innings_runs():
    return ipl_df.pivot_table(values='runs', index=['match_code','inning'], aggfunc=np.sum)
# Solution
