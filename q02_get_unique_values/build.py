from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

#Solution
import numpy as np
def get_unique_venues():
    venue_array = np.array(ipl_df['venue'].value_counts().index)
    return venue_array
