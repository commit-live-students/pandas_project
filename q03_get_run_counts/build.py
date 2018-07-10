# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
import pandas as pd

def get_run_counts():

    runs_count = ipl_df['runs'].value_counts(sort= True)
    return runs_count

get_run_counts()
