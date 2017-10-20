from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

#Solution
def get_unique_venues():
    return np.unique(ipl_df.venue)
print get_unique_venues()
