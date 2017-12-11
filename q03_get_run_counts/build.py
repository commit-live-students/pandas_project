import pandas as pd
from pandas import DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

#On the 'runs' Series apply the value_counts() to get the count of each value in 'runs' column
def get_run_counts():
    runs_count = ipl_df['runs'].value_counts()

    return runs_count
