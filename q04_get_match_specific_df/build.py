from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
#df = ipl_df.set_index('match_code')
#print df[:10]

# Solution
def get_match_specific_df(mtch_code=598057):
    match_df = ipl_df.loc[ipl_df['match_code'] == mtch_code]
    return match_df
print get_match_specific_df(598057)
