# Default imports
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def create_bowler_filter(bowler):

    #ipl_df1 = pd.Series(ipl_df['bowler'])
    bowler_fill = Series(ipl_df['bowler'] == bowler)

    #return ipl_df1
    return bowler_fill
print create_bowler_filter('AB Dinda')
