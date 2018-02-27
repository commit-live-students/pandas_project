import numpy as np
import pandas as pd
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_run_counts():
    runs = ipl_df.runs
    runs_counts = runs.value_counts(normalize= False, sort = True, ascending= False)
    return runs_counts

get_run_counts()
