# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
# ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

import pandas as pd
def get_match_innings_runs () :
    #path = path
    a = pd.read_csv("data/ipl_dataset.csv")
    #b = list(a.columns.values)
    #inningsum = a['runs'].groupby(a['match_code','inning']).sum()
    df = a.groupby(['match_code', "inning"]).runs.sum()
    #print inningsum
   # print a[match_code],[]
   # df = a[(a.bowler == bowler)]
   # filter = (a['bowler'] == bowler)
    #print a
    return df

# Solution
