import pandas as pd
import numpy as np
from pandas import DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

#Solution
def get_unique_venues():
    df = DataFrame(ipl_df)
    df1 =  df['venue']
    a = df1.unique()
    venues = np.array(a)

    return venues

    #np.array()
    #df_unq =  df1.unique()

    #print df_unq.size



#print get_unique_venues()
