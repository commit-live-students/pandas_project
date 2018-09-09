from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

def get_unique_venues():
    
    venues = ipl_df['venue'].unique()
    
    return venues

from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

def get_unique_venues():
    
    venues = ipl_df['venue'].unique()
    
    return venues





