# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
import pandas as pd
import numpy as np
def get_runs_counts_by_match() :
    #path = path
    run = np.array([0,1,2,3,4,5,6])
    a = pd.read_csv("data/ipl_dataset.csv")
    df = a.pivot_table(
                index='match_code',
                columns= ['runs'],
                values='date',
                aggfunc= 'count',fill_value = 0)
    #pivot_df= a.pivot_table(df, values = 'run', index=['match_code'], columns = 'match_code')
    return df
