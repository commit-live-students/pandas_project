# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():

    data = ipl_df.pivot_table('runs',aggfunc = len ,index = ipl_df['match_code'],
                       columns = ipl_df['runs'])

    return data
