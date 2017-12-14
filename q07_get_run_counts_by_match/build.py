import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Use the pivot_table feature from pandas to slice column match_code and runs using .loc function and aggregate the occurences
# of respective runs (columns = runs) using numpy's count function
def get_runs_counts_by_match():
    df = pd.pivot_table(ipl_df.loc[:,['match_code','runs']], index=['match_code'], columns = 'runs', aggfunc=np.count_nonzero)
    return df
