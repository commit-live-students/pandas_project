# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    df1 = pd.Series(ipl_df['runs'])
    df2 = np.unique(df1, return_counts=True)
    df3 = pd.Series(data = df2[1], index = df2[0])
    return df3
