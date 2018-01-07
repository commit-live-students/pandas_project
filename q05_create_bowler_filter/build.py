# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
def create_bowler_filter(bowler_name):
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    bowler_series = ipl_df['bowler'] == bowler_name
    return bowler_series


# Solution
