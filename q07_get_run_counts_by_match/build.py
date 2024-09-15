import pandas as pd
from pandas import pivot_table
import numpy as np

def get_runs_counts_by_match():
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    ans=pivot_table(ipl_data,values=['batsman'], index=['match_code'],columns=['runs'],aggfunc='count')
    return ans

ans=get_runs_counts_by_match()
ans

