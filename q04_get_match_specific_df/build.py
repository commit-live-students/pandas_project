# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution

def get_match_specific_df(match_code):
    
    #checking type of data in match_code
    #print(type(ipl_df['match_code'][0]))
    
    #match_code == ipl_df['match_code'][0] #output is true 
    
    # result of particular match_code
    result = ipl_df[ipl_df['match_code']== match_code]
    
    return result

match_code = 392203
get_match_specific_df(match_code)


