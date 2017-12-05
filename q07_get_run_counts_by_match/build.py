# Default Imports
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    data1=ipl_df[['match_code','runs']]
    data1['count']=1
    frequency=data1.pivot_table('count', aggfunc=np.sum, index='match_code', columns='runs')
    return frequency
