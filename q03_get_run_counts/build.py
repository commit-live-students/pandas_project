# Default Imports
import numpy as np
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    df = pd.DataFrame(ipl_df['runs'])
    df['count'] = 1
    run_pivot = df.pivot_table('count', aggfunc=np.sum, index='runs')
    run_series = pd.Series(run_pivot['count'], index=run_pivot.index)
    return run_series
print get_run_counts()
