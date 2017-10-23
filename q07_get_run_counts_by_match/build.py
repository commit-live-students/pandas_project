# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
import pandas as pd
# Solution
def get_runs_counts_by_match():
    #return ipl_df.pivot_table(index=['match_code'], values=['bowler'], columns=['runs'], aggfunc='count')
    return ipl_df.groupby(["match_code", 'runs'])['runs'].count().unstack()
