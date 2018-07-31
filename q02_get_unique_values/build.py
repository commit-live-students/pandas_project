# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

def get_unique_venues():
    ipl=pd.DataFrame(ipl_df)
    venues=ipl.venue.unique()
    return venues

get_unique_venues()


