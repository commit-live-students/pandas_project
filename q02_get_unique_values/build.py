from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

#Solution
#print ipl_df[:5]
def get_unique_venues():
    ary = np.array(ipl_df['venue'].unique())
    return ary
print get_unique_venues()
