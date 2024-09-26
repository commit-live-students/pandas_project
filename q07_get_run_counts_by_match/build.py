from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_runs_counts_by_match():
    pivot_df = pd.pivot_table(ipl_df, index = 'match_code', values = 'batsman', columns = 'runs', aggfunc='count', fill_value=0)
    
    return pivot_df

get_runs_counts_by_match()





