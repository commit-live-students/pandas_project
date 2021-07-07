# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = pd.read_csv('./data/ipl_dataset.csv')
#ipl_df = ipl_df.set_index('match_code')
def get_match_specific_df(match_code):
    df= ipl_df.loc[ipl_df['match_code']==match_code]
    return df
#Test cases
# get_match_specific_df(335987)


    
    



