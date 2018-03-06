# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

def get_match_innings_runs():
    d1 = ipl_df.groupby(by= ['match_code','inning'])['runs'].sum()
    d2 = pd.DataFrame(d1)
    return d2

get_match_innings_runs()
