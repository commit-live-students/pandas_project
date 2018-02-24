# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    #newcdf.pivot_table('Temp', aggfunc=np.max, index='Year')
    runs_per_match = pd.pivot_table(data=ipl_df.loc[:,['match_code', 'runs']], columns=ipl_df.loc[:,'runs'], aggfunc='count', index='match_code')
    return runs_per_match

get_runs_counts_by_match()
