import numpy as np
import pandas as pd
from pandas import DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
match_code=598057
def get_match_specific_df(match_code):
    data_match_code=ipl_df[ipl_df['match_code']==match_code]
    return data_match_code
