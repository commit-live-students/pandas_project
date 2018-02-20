# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

import numpy as np


def get_runs_counts_by_match():

    ipl_df['count'] = 1
    table = ipl_df.pivot_table( 'count' , aggfunc=np.sum, index='match_code' , columns=['runs'])
    return table

get_runs_counts_by_match()
