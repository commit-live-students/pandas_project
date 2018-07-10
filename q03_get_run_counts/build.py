# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
from pandas import DataFrame, Series

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    run_freq = ipl_df.groupby(['runs'],axis=0)
    run_freq_series = run_freq['runs'].count()
    return run_freq_series

s1 = get_run_counts()
print type(s1)
print s1
