import pandas as pd

def get_run_counts():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    ans=ipl_data['runs'].value_counts()
    return ans


