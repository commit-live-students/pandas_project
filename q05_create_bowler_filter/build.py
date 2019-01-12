# %load q05_create_bowler_filter/build.py
# Default imports
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution



def create_bowler_filter (name):
    for x in ipl_df['bowler'] :
        s = pd.Series( index = list(x))
        logical_results = str(s) == name
        #logical_results_series = pd.Series(np.arange(0,8),index=logical_results)
        new = s[logical_results]
        return new
    #bow_array =pd.Series
# for x in ipl_df['bowler']:
 #       ipl_df['bowler'] == name
  #      bow_array = pd.Series(True)
   # return bow_array
create_bowler_filter('AB Dinda')

s = pd.Series(  index = list(ipl_df['bowler']))
s


















