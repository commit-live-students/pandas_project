# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution

def create_bowler_filter(name):
    bowler_check=ipl_df['bowler']==name
    return bowler_check
create_bowler_filter('I Sharma') 



