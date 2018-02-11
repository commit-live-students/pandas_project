# Default Imports
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    runs=ipl_df['runs']
    unique_runs=pd.unique(runs)
    frequency_runs=pd.value_counts(runs)
    s1=Series(frequency_runs,index=unique_runs,dtype=np.int32)
    return s1
