# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    runs = ipl_df.runs
    #print runs

    run_count = np.unique(runs, return_counts=True)
    #print run_count

    run_freq = pd.Series(run_count[1], index=run_count[0])
    #print run_freq
    return run_freq

get_run_counts()
