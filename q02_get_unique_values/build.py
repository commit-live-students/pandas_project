# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
import pandas as pd
#Solution
def get_unique_venues():
    a=read_csv_data_to_df('data/ipl_dataset.csv')
    a=a['venue'].unique()
    return (a)

c=get_unique_venues()
c


