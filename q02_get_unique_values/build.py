# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
def get_unique_venues():
    ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
    unique_venues = ipl_df['venue'].unique()
    return unique_venues
#Solution
get_unique_venues()

