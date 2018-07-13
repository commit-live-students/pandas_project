import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_innings_runs():
    #print ipl_df.columns
    grouped =  ipl_df.groupby(['match_code','inning'])
    return grouped['runs'].agg(np.sum)
#get_match_innings_runs()
