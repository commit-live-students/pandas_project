# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Funtion define
def get_match_innings_runs():
    '''Total runs made in each inning of each match'''
    data = ipl_df[['match_code','inning','runs']].groupby(['match_code','inning']).sum()
    return data
    
 # Funtion call   
get_match_innings_runs()


