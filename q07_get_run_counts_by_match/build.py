# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

import pandas as pd
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Function define
def get_runs_counts_by_match():
    ''' function to create pivot table count of runs per match '''
    ipl_df['runs2'] = ipl_df['runs']
    df = ipl_df.pivot_table(values = 'runs' ,
                                      columns = 'runs2',
                                      index = 'match_code' ,
                                      aggfunc = np.size)
    return df

#Function call 
get_runs_counts_by_match()




