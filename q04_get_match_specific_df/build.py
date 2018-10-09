# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_match_specific_df(match_code):
    #creating a filter for the given match code through the function
    match_code_filter = ipl_df['match_code']==match_code
    #applying the above created filter to the main data frame and assigining it to a variable
    match_info=ipl_df[match_code_filter]
    return match_info





