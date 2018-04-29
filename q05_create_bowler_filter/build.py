import pandas as pd

def create_bowler_filter(name):
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    return (ipl_data['bowler']==name)

