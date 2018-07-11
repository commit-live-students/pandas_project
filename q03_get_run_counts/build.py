# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
import pandas as pd
def get_run_counts():
    df_runs = ipl_df[['match_code','runs']].groupby('runs').count()
    runs_count = pd.Series(df_runs['match_code'])
    return runs_count

# rcount = get_run_counts()
# print rcount
# print type(get_run_counts())
