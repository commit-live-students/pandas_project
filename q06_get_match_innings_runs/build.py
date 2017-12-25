import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    #df = pd.DataFrame(ipl_df)
    grp_match = ipl_df[['match_code', 'inning', 'runs']].groupby(['match_code', 'inning', 'runs'])['runs'].sum()

    #group_matches = df.rolling(window = 3, min_periods = 1)
    return grp_match
    #return group_matches[['match_code', 'inning', 'runs']].aggregate(np.sum)

print get_match_innings_runs()
