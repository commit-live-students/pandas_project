# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    df_tmp = ipl_df[['match_code','inning','runs']]
    ptable = pd.pivot_table(data=df_tmp, index=['match_code','runs'],values='runs',aggfunc='count')
    df_run_count_match = ptable.unstack().fillna(0)
    return df_run_count_match
