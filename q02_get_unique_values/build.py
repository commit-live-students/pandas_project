# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
ipl = pd.read_csv('data/ipl_dataset.csv')
#Solution
def get_unique_venues():
    a = ipl['venue'].unique()
    return a

    


