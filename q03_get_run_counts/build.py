# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
from pandas import Series, DataFrame
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    runs_counts = ipl_df['runs'].value_counts()
    return(runs_counts)
print(get_run_counts())
