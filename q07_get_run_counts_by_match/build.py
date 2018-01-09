import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from pandas import Series, DataFrame

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():
    ipl_df['count']=1
    return ipl_df.pivot_table('count',aggfunc=np.sum, index=['match_code'],columns='runs')
