# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
def get_match_innings_runs():
    df = ipl_df
    return df.loc[:, ['runs']]
    #l=df.groupby(['match_code','inning','runs'])
    #return l

    



df=ipl_df
df.loc[:, ['runs','match_code', 'inning']]

d=get_match_innings_runs()
d.sum()
type(d.sum())
l=df.groupby(['match_code','inning','runs'])
l.sum()


