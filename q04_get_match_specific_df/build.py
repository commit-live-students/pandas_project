# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

import pandas as pd
def get_match_specific_df(match_code) :
    #path = path
    a = pd.read_csv("data/ipl_dataset.csv")
    df = a[(a.match_code == match_code)]
    #print a
    return df
