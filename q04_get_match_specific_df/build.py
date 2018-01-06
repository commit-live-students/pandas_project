# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
def get_match_specific_df(match_code):
    if type(match_code) == int:
        return ipl_df[ipl_df['match_code'] == match_code]
    else:
        print 'Not an integer'

# Solution
