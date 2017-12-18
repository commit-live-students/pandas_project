# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    data=ipl_df[['match_code','runs']]
    data.loc[:,'count']=np.ones(1)
    return data.pivot_table('count', aggfunc=np.sum, index='match_code', columns='runs').fillna(0)
