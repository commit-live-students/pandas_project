# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

d = {'match_code': [], 'inning': [], 'runs': []}
df = pd.DataFrame(data=d)

df['match_code'] = ipl_df['match_code'].unique()

# Solution
def get_match_innings_runs():
    return ipl_df.groupby(['match_code', 'inning'])['runs'].sum()

get_match_innings_runs().sum()




