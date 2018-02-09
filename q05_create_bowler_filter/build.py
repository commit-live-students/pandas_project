# Default imports
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.

ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
# Solution
def create_bowler_filter(bowler):
    df = ipl_df.loc[:,'bowler']
    n1 = np.array(df)
    n2 = np.where(n1 == bowler,True,False)
    df1 = pd.Series(n2)

    return df1




print create_bowler_filter('M Muralitharan')
