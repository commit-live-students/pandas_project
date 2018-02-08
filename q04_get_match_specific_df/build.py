import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    df = ipl_df.loc[ipl_df['match_code'] == match_code]
    return df

    #df = DataFrame(ipl_df)
    #dff = df['match_code']
    #print type(dff)
    #df_new = df.loc[df['match_code'] == match_code]
    #print type(ipl_df)
#print get_match_specific_df(392203)
