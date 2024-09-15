import pandas as pd

def get_match_innings_runs():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    ans=ipl_data.groupby(by=['match_code','inning'])['runs'].sum()
    return ans

ans2=get_match_innings_runs()
ans2


