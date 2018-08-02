# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
def  get_match_innings_runs():
    df=ipl_df
    df=pd.DataFrame(df)
    a=pd.DataFrame(df.groupby(['inning','match_code']).runs.sum())
    return a



a=get_match_innings_runs()
a


