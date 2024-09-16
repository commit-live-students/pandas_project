# %load q05_create_bowler_filter/build.py
# Default imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
def create_bowler_filter(bowler): 
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
    bowler_df = ipl_df.loc[ipl_df['bowler'] == bowler]
    bowler_series = pd.Series(bowler_df['bowler'])
    return bowler_series.count()
# Solution
create_bowler_filter('I Sharma')


