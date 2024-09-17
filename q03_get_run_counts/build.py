# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
import pandas as pd
from pandas import Series
def get_run_counts():
    
    runs_index= [0,1,2,3,4,5,6]
    data = [0,0,0,0,0,0,0]
    main_series = Series(data,runs_index)
    for i in range(len(ipl_df)):
        runs = ipl_df['runs'][i]
        main_series[runs] = main_series[runs] + 1 
    return main_series
    



#type(main_series)


