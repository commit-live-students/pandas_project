from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

import numpy as np

def get_unique_venues():

    venue = ipl_df['venue']

    unique = np.unique(venue)
    return unique

get_unique_venues()
