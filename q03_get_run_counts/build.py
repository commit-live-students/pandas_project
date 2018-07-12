import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from pandas import Series, DataFrame

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_run_counts():
    ipl_df['count_run']=ipl_df['runs']
    lr= ipl_df.pivot_table('count_run',aggfunc=np.size, index=['runs'])
    get_run = Series.tolist(lr['count_run'])
    lst_index=[]
    for i in lr.index:
        lst_index.append(i)
    return pd.Series(get_run,index=lst_index)
