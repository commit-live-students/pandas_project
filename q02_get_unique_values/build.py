# %load q02_get_unique_values/build.py
import pandas as pd
import numpy as np
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

#Solution
def get_unique_venues():
    
    return(pd.unique(ipl_df['venue']))
    
    
    
#get_unique_venues()  
    

