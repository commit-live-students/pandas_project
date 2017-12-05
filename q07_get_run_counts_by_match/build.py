# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
import pandas as pd
# Solution
def get_runs_counts_by_match():
    new_df = pd.DataFrame(columns=['match_code','0','1','2','3','4','5','6'])
    new_df['match_code']=ipl_df['match_code']
    new_df['0']=ipl_df['runs']==0
    new_df['1']=ipl_df['runs']==1
    new_df['2']=ipl_df['runs']==2
    new_df['3']=ipl_df['runs']==3
    new_df['4']=ipl_df['runs']==4
    new_df['5']=ipl_df['runs']==5
    new_df['6']=ipl_df['runs']==6
    pivot_df=new_df.pivot_table(['0','1','2','3','4','5','6'],index=['match_code'],aggfunc='sum')
    return pivot_df
