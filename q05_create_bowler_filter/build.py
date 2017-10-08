# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution

def create_bowler_filter(bowler):
    bowler_Series=ipl_df['bowler']
    bowler_filter =bowler_Series==bowler
    #bowler_Series_filter=bowler_Series[bowler_filter]
    #print(type(bowler_filter))
    return bowler_filter
