# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

import pandas as pd
def get_run_counts() :
    path = "data/ipl_dataset.csv"
    #path = path
    ipl_df = pd.read_csv(path)
    runs_count = ipl_df['match_code'].groupby(ipl_df['runs']).count()
    #unq = ipl_df[:]
    return runs_count


# Solution
