# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Funtion define 
def get_unique_venues():
    ''' get unique venues'''
    return ipl_df['venue'].unique()

#funtion call
get_unique_venues()


