from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
# ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

import pandas as pd
def get_unique_venues() :
    path = "data/ipl_dataset.csv"
    #path = path
    ipl_df = pd.read_csv(path)
    #print(ipl_df)
    unq = ipl_df.venue.unique()
    return unq

#Solution
