# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = pd.read_csv("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    matc_specific = ipl_df[ipl_df['match_code'] == match_code]
    return matc_specific
#get_match_specific_df(match_code = '335983')
