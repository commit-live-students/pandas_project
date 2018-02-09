# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_match_specific_df(match_code):
    
    data = DataFrame(ipl_df)
    df = data[data['match_code'] == match_code]
    return df
    
    #also works because of as same indexing properties
    #df = ipl_df.loc[ipl_df['match_code'] == match_code]
    #return df
    

