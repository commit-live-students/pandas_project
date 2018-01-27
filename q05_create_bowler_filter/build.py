# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def create_bowler_filter(bowler):
    df1 = ipl_df.loc[:, 'bowler']
    n1 = np.array(df1)
    n2 = np.where(n1 == bowler, True, False)
    df2 = pd.Series(n2)
    return df2
