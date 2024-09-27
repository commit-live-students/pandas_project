# %load q04_get_match_specific_df/build.py
#from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

import numpy as np
import pandas as pd
ifl_df=pd.read_csv('./data/ipl_dataset.csv')


def get_match_specific_df(match_code):
   
    

    #df=ifl_df[(ifl_df['match_code']==match_code)]
    df=ifl_df[ifl_df.match_code==match_code]
    return df

get_match_specific_df(598057)





