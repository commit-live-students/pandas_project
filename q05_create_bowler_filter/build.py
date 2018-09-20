# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def create_bowler_filter(bowler_name):
    
    #checking whether type of data in bowler column same or not
    #print(ipl_df['bowler'][0]== bowler_name )
    
    # returning filter result
    result = ipl_df['bowler'] == bowler_name
    
    return result
bowler_name = 'I Sharma'
create_bowler_filter(bowler_name)


