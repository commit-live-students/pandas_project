#%load q03_get_run_counts/build.py

import pandas as pd
path='./data/ipl_dataset.csv'

def get_run_counts():
    df=pd.read_csv(path)

    grp=df.groupby(df.runs)['runs'].count()

    #print(type(grp))
    return grp


