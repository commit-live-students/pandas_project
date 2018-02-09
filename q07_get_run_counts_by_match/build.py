# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():

    runs_df = ipl_df[['match_code', 'runs']]
    runs_df['count'] = 1
    runs_pivot = runs_df.pivot_table('count', aggfunc=np.sum, index='match_code', columns='runs').fillna('NA')
    #runs_pivot = runs_df.pivot_table('count', aggfunc='count', index='match_code', columns='runs')
    return runs_pivot



'''def get_runs_counts_by_match():

    df = pd.pivot_table(data=ipl_df.loc[:,['match_code', 'runs']], index='match_code', columns=ipl_df.loc[:,'runs'], aggfunc='count')

    return df'''


print get_runs_counts_by_match()
