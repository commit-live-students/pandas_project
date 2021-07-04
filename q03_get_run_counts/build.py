# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_run_counts():
    
    # calculate the frequency of values in column runs
    frequency_of_runs = ipl_df['runs'].value_counts()
    
    return frequency_of_runs


get_run_counts()


