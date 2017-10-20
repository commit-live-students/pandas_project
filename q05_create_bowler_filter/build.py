# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

# Solution
def create_bowler_filter(bowler):
    filter = ipl_df['bowler'] == 'I Sharma'
    return filter
print create_bowler_filter(bowler = 'I Sharma')
