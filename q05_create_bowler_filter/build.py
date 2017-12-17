# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
def create_bowler_filter(name):
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    bowlers = ipl_df['bowler'] == name
    #print type(bowlers)
    return bowlers
