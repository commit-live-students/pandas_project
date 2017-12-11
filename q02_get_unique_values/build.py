import pandas as pd
from pandas import DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

#Use the Unique() feature supported for DataFrame in Pandas (on the venue column from the ipl_dataset.csv)
def get_unique_venues():
    venues = ipl_df.venue.unique()

    return venues
