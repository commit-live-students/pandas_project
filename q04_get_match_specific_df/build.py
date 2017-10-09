# %load q04_get_match_specific_df/build.py
# Default imports
import pandas as pd
#from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
#ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(match_code):
    ipl_df = pd.read_csv("./data/ipl_dataset.csv")
    return ipl_df[ipl_df['match_code'] ==match_code ]
