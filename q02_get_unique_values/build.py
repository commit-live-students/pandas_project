import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

#Solution
def get_unique_venues():
    venues = pd.DataFrame(ipl_df)
    #venues_pl = venues['venue']
    venues_pl = Series.unique(venues['venue'])

    return (venues_pl)
print get_unique_venues()
