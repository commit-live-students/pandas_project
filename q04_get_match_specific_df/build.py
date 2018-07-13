from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(match_code):
     #print ipl_df.match_code.dtype
     return ipl_df.loc[ipl_df.match_code == match_code]
#print type(get_match_specific_df(598057))
