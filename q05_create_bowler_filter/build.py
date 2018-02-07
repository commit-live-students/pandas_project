# Default imports
import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
#print ipl_df.head()

# Solution
def create_bowler_filter(bowler_filter='I Sharma'):
    ary = (ipl_df['bowler'].astype(np.str) == 'I Sharma')
    return ary.sum()
print create_bowler_filter()
