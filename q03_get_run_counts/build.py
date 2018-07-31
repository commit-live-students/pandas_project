# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_run_counts():
    
    
    ipl=pd.DataFrame(ipl_df)
    runs_count=pd.Series(ipl['runs'].value_counts())
    return runs_count
    


get_run_counts()


