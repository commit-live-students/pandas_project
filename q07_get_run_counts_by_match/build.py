# Default Imports
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame



from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    counts_by_match=ipl_df.pivot_table(values='inning',columns=['runs'],aggfunc=np.sum,index='match_code')
    return counts_by_match
