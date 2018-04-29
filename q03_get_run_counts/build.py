# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
ipl_df.head(2)
# Solution
def get_run_counts():
    runSeries = pd.Series(ipl_df['runs'])
    print(runSeries.value_counts())
    return runSeries.value_counts()

get_run_counts()

