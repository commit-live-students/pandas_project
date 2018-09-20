# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

#Solution
def get_unique_venues():  
    
    # get unique values from venue column
    unique_venue = ipl_df['venue'].unique()
    
    return unique_venue


get_unique_venues()
#pd.set_option('display.max_row', 1000)
#pd.set_option('display.max_columns',10)



