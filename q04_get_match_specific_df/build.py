# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(match_code):
    matchrecords = ipl_df[ipl_df['match_code'] == match_code]
    return matchrecords
