# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
import pandas as pd
from pandas import Series
def get_match_innings_runs():
    df = pd.DataFrame({'match_code':[],'innings':[],'runs':[]})
    matches_array = ipl_df.match_code.unique()
    for i in range(len(matches_array)):
        runs_1 = sum(ipl_df[ipl_df['match_code']==matches_array[i]][ipl_df['inning']==1]['runs']) 
        runs_2 = sum(ipl_df[ipl_df['match_code']==matches_array[i]][ipl_df['inning']==2]['runs'])
        main_match_code = matches_array[i]
        dict1 = {'match_code':main_match_code,'innings':1,'runs':runs_1}
        dict2 = {'match_code':main_match_code,'innings':2,'runs':runs_2}
        #print(list1)
        df = df.append(dict1,ignore_index=True)
        df = df.append(dict2,ignore_index=True)
    return df.runs
get_match_innings_runs().sum()





