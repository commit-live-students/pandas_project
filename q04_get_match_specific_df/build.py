# %load q04_get_match_specific_df/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
#print(ipl_df)
match_code=598057

def get_match_specific_df(match_code):
    s1=ipl_df[ipl_df['match_code']==match_code]
    #print(s1.shape)
    return (s1)

get_match_specific_df (match_code)
