import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():
    ipl_df["frequency"] = 1
    proj_ipldf = ipl_df[['match_code','runs','frequency']]
    pivot_ipldf=proj_ipldf.pivot_table('frequency',aggfunc=np.sum,index='match_code',columns='runs').fillna(0)
    return pivot_ipldf
