# %load q03_get_run_counts/build.py
# Default Imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_run_counts():
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

    runs_series = pd.Series(index=ipl_df['runs'].unique(),data=ipl_df['runs'].value_counts())
    return runs_series

get_run_counts()


