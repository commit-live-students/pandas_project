import pandas as pd

def get_unique_venues():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    return ipl_data['venue'].unique()

ans=get_unique_venues()
ans
    


