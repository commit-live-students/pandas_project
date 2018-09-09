# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    df = pd.pivot_table(ipl_df,index='match_code',columns='runs',aggfunc='count')['batsman']
    return df


# columnss = ipl_df['runs'].unique()
# list(columnss)
# rowss = ipl_df['match_code'].unique()
# list(rowss)
#dff = ipl_df.groupby('match_code').count()
df = pd.pivot_table(ipl_df,index='match_code',columns='runs',aggfunc='count')['batsman']
df


