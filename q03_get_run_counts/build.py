# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_run_counts ():
    counts=ipl_df.runs.value_counts()
    #print(counts)
    s=counts.sort_index()
    #print(s)
    s1=pd.Series(counts,index=s.index).unique()
    #print(s1.shape)
    return (s1)

get_run_counts ()
