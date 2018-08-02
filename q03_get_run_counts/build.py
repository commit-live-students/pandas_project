# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
import pandas as pd
# Solution
def get_run_counts():
    a=ipl_df['runs']
    a=pd.Series(a.value_counts(),index=a)
    s=a.groupby(a.index).first()
    return s
c=get_run_counts()
c


