# Default Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    pddf = pd.pivot_table(ipl_df, index=ipl_df["match_code"], columns=ipl_df["runs"], values = "runs", aggfunc="count").fillna(0)
    return pddf
