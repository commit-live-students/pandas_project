#%load q07_get_run_counts_by_match/build.py


import pandas as pd
import numpy as np

df=pd.read_csv('./data/ipl_dataset.csv')
#df.columns
def get_runs_counts_by_match():
    
    df1=df.pivot_table(index='match_code',columns='runs',values='batsman',aggfunc='count')    

    return df1

get_runs_counts_by_match()
# gr=df.groupby('match_code')  
# gr['runs'].sum()


