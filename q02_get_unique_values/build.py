# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given the dataset already in 'ipl_df'.

#Solution
def get_unique_venues():
    
    ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
    return ipl_df['venue'].unique()

get_unique_venues()


