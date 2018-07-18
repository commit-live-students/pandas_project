# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd 
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    pivot = pd.pivot_table(ipl_df,index='match_code',columns='runs',aggfunc='count')
    return pivot.iloc[:,:7]
