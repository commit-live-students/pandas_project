# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def create_bowler_filter(bowler):
    loc_string = ipl_df.loc[:, 'bowler']
    string_to_array = np.array(loc_string)
    bowlers_name = np.where(string_to_array == bowler, True, False)
    conv_series = pd.Series(bowlers_name)
    return conv_series

#print (type(create_bowler_filter(0)))
#print (create_bowler_filter(0))
