# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    match_run_series=ipl_df[['match_code','runs']]
    match_run_pivot=pd.pivot_table(ipl_df,values=['inning'],
                                      index=['match_code'],
                                      columns=['runs'],
                                      aggfunc='count')
    return match_run_pivot
    #print(ipl_df.head(5))


#ipl_df.info()  
