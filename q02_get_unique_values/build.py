import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
def get_unique_venues():
    venue = ipl_df.loc[0:]['venue']
    return pd.unique(venue)
