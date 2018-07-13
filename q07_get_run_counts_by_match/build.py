# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    data = pd.pivot_table(data=ipl_df, columns='runs', index='match_code', aggfunc='count', fill_value=0, values='inning')
    return data
