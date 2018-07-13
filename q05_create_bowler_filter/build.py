# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
from pandas import Series
# Solution

def create_bowler_filter(bowler):
    bool_array = Series(ipl_df['bowler'][ipl_df['bowler'] == bowler], dtype = bool)
    return bool_array

actual = create_bowler_filter('I Sharma')
